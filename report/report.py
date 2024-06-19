import numpy as np
import pylatex as pl
import pandas as pd
# import analysis.A3_Obesity as obes
import A3__Obesity as obes
# import analysis.A3_GDP as gdp


geometry_options = {"tmargin": "2cm", "lmargin": "2cm"}
doc = pl.Document(geometry_options=geometry_options)
doc.packages.append(pl.Package('booktabs'))
doc.preamble.append(pl.Command('title', 'Relatório de Dados - GDP e Obesidade'))
doc.preamble.append(pl.Command('author', 'Rafael Rodrigues, João Purificaçao'))
doc.preamble.append(pl.Command('date', pl.NoEscape(r'\today')))
doc.append(pl.NoEscape(r'\maketitle'))


with doc.create(pl.Section('Obesidade')):
    with doc.create(pl.Subsection('Estrutura')): 
        with doc.create(pl.Table(position='htbp')) as table:
            # table.add_caption('Tabela de Obesidade')
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.obesity.head().to_latex(float_format="%.2f",escape=True,index=False)))
    with doc.create(pl.Subsection('Comparação entre Homens e Mulheres:')):
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.relaction_mf.to_latex(float_format="%.2f",escape=True)))
            table.add_caption('Relação entre os Sexos')
    with doc.create(pl.Subsection('Percentuais na Ámerica do Norte:')):
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.mean_nort_2010.to_latex(float_format="%.2f",escape=True)))
            table.add_caption('Média do Países por Sexo')
doc.append(pl.NewPage())
with doc.create(pl.Subsection('Taxa de Aumento dos Índices de Obesidade:')):
    with doc.create(pl.Subsubsection('Variação em 2010:')):
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.max_tax_2010.to_latex(float_format="%.2f",escape=True,index=False)))
            table.add_caption('Maior Aumento de Taxa entre países em 2010')
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.min_tax_2010.to_latex(float_format="%.2f",escape=True,index=False)))
            table.add_caption('Menor Aumento de Taxa entre países em 2010')
    with doc.create(pl.Subsubsection('Variação em 2016:')):
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.max_tax_2016.to_latex(float_format="%.2f",escape=True,index=False)))
            table.add_caption('Maior Aumento de Taxa entre países em 2016')
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.min_tax_2016.to_latex(float_format="%.2f",escape=True,index=False)))
            table.add_caption('Menor Aumento de Taxa entre países em 2016')

doc.append(pl.NewPage())

with doc.create(pl.Subsubsection('Variação no período completo:')):
    with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.max_tax_all.to_latex(float_format="%.2f",escape=True,index=False)))
            table.add_caption('Maior Aumento de Taxa entre países')
    with doc.create(pl.Table(position='htbp')) as table:
        table.append(pl.Command('centering'))
        table.append(pl.NoEscape(obes.min_tax_all.to_latex(float_format="%.2f",escape=True,index=False)))
        table.add_caption('Menor Aumento de Taxa entre países')

doc.append(pl.NewPage())
with doc.create(pl.Subsection('Apanhando sobre o Brasil:')):
    with doc.create(pl.Subsubsection('Variação em 2010:')):
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(obes.mean_nort_2010.to_latex(float_format="%.2f",escape=True)))
            table.add_caption('Média do Países por Sexo')
doc.append(pl.NewPage())
with doc.create(pl.Section('GDP')):
    with doc.create(pl.Subsection('Dados')):
        with doc.create(pl.Figure(position='htbp')) as plot_teste:
            plot_teste.add_image('img/foo.png', width='300px')
            plot_teste.add_caption('Look it\'s on its back')




doc.generate_tex('report/tex/report')
doc.generate_pdf('report',compiler='C:/Users/joao44379/AppData/Local/Programs/MiKTeX/miktex/bin/x64/miktex-texworks.exe')
# doc.generate_pdf('report',compiler='C:/Users/joao44379/AppData/Local/Programs/MiKTeX/miktex/bin/x64/miktex-console.exe')