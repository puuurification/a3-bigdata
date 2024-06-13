from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape


def fill_document(doc):
    texto_introducao = '''
    O projeto programado para a avaliação A3 da materia de Análise de Dados e BigData ministrada pelo Professor Euclério tratou-se da analise de dois datasets, mais abordados futuramente, este documento apresenta não somente o resumo das solicitações, como respostas as perguntas norteadoras, como também demonstrações e explanações do processo feito
    '''

    with doc.create(Section('Introdução')):
        doc.append(texto_introducao)
    
        with doc.create(Subsection('Dataset de Obesidade')):
            doc.append('Also some crazy characters: $&#{}')
        
        with doc.create(Subsection('Dataset de GDP')):
            doc.append('Also some crazy characters: $&#{}')

    with doc.create(Section('Limpeza dos DataSets')):
        doc.append('Some text. dentro da função')

        with doc.create(Subsection('Obesidade')):
            doc.append('Also some crazy characters: $&#{}')
        
        with doc.create(Subsection('GDP')):
            doc.append('Also some crazy characters: $&#{}')
    
    with doc.create(Section('Respostas')):
        doc.append('Some text. dentro da função')



if __name__ == '__main__':
    # Basic document
    doc = Document('basic')
    fill_document(doc)

    # doc.generate_pdf(clean_tex=False)
    # doc.generate_tex()

    # Document with `\maketitle` command activated
    doc = Document()

    doc.preamble.append(Command('title', 'Relatório de Dados - GDP e Obesidade'))
    doc.preamble.append(Command('author', 'Rafael Rodrigues, João Purificaçao'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    # doc.generate_pdf('basic_maketitle', clean_tex=False)


    # doc.generate_pdf('basic_maketitle2', clean_tex=False)
    doc.generate_tex('report/tex/basic_maketitle3')
    tex = doc.dumps()  # The document as string in LaTeX syntax