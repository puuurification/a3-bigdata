import numpy as np
import pylatex as pl
import pandas as pd

# from pylatex import Document, Section, Subsection, Command
# from pylatex.utils import italic, NoEscape


def fill_document(doc):
    texto_introducao = '''
    O projeto programado para a avaliação A3 da materia de Análise de Dados e BigData ministrada pelo Professor Euclério tratou-se da analise de dois datasets, mais abordados futuramente, este documento apresenta não somente o resumo das solicitações, como respostas as perguntas norteadoras, como também demonstrações e explanações do processo feito
    '''

    with doc.create(pl.Section('Introdução')):
        doc.append(texto_introducao)

        with doc.create(pl.Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')

    with doc.create(pl.Section('A second section')):
        doc.append('Some text. dentro da função')



# if __name__ == '__main__':
# Basic document
doc = pl.Document('basic')
fill_document(doc)

# doc.generate_pdf(clean_tex=False)
# doc.generate_tex()

# Document with `\maketitle` command activated
doc = pl.Document()

doc.preamble.append(pl.Command('title', 'Relatório de Dados - GDP e Obesidade'))
doc.preamble.append(pl.Command('author', 'Rafael Rodrigues, João Purificaçao'))
doc.preamble.append(pl.Command('date', pl.NoEscape(r'\today')))
doc.append(pl.NoEscape(r'\maketitle'))

fill_document(doc)

# doc.generate_pdf('basic_maketitle', clean_tex=False)


# doc.generate_pdf('basic_maketitle2', clean_tex=False)
doc.generate_tex('report/tex/final-tex')
tex = doc.dumps()  # The document as string in LaTeX syntax