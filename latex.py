import numpy as np
import pylatex as pl
import pandas as pd
import relatorio as rel


geometry_options = {"tmargin": "2cm", "lmargin": "2cm"}
doc = pl.Document(geometry_options=geometry_options)
doc.packages.append(pl.Package('booktabs'))
doc.preamble.append(pl.Command('title', 'Relatório de Dados - GDP e Obesidade'))
doc.preamble.append(pl.Command('author', 'Rafael Rodrigues, João Purificaçao'))
doc.preamble.append(pl.Command('date', pl.NoEscape(r'\today')))
doc.append(pl.NoEscape(r'\maketitle'))

with doc.create(pl.Section('Obesidade')):
    with doc.create(pl.Subsection('Comparação entre Homens e Mulheres:')):
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(rel.df_union_describe_sexes.to_latex(float_format="%.2f",escape=True)))
            table.add_caption('Relação entre os Sexos')
        doc.append(pl.NoEscape(rel.union_describe_sexes))
    with doc.create(pl.Subsection('Percentuais na Ámerica do Norte:')):
        with doc.create(pl.Table(position='htbp')) as table:
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(rel.df_north_america_mean_2010.to_latex(float_format="%.2f",escape=True,index=False)))
            table.add_caption('Média de Obesidade por Sexo na América do Norte em 2010')
doc.append(pl.NewPage())
with doc.create(pl.Subsection('Taxa de aumento de índices de obesidade em 2010')):
    with doc.create(pl.Table(position='htbp')) as table:
        table.append(pl.Command('centering'))
        table.append(pl.NoEscape(rel.df_max_tax_obes_2010.to_latex(float_format="%.2f",escape=True,index=False)))
        table.add_caption('Maior aumento em 2010')
    with doc.create(pl.Table(position='htbp')) as table:
        table.append(pl.Command('centering'))
        table.append(pl.NoEscape(rel.df_min_tax_obes_2010.to_latex(float_format="%.2f",escape=True,index=False)))
        table.add_caption('Menor aumento em 2010')
with doc.create(pl.Subsection('Taxa de aumento de índices de obesidade em 2016')):            
    with doc.create(pl.Table(position='htbp')) as table:
        table.append(pl.Command('centering'))
        table.append(pl.NoEscape(rel.df_max_tax_obes_2016.to_latex(float_format="%.2f",escape=True,index=False)))
        table.add_caption('Maior aumento em 2016')
doc.append(pl.NewPage())
with doc.create(pl.Table(position='htbp')) as table:
    table.append(pl.Command('centering'))
    table.append(pl.NoEscape(rel.df_min_tax_obes_2016.to_latex(float_format="%.2f",escape=True,index=False)))
    table.add_caption('Menor aumento em 2016')
with doc.create(pl.Subsection('Taxa de aumento de índices de obesidade no período completo')): 
    with doc.create(pl.Table(position='htbp')) as table:
        table.append(pl.Command('centering'))
        table.append(pl.NoEscape(rel.df_max_tax_obes.to_latex(float_format="%.2f",escape=True,index=False)))
        table.add_caption('Maior aumento no período completo')
    with doc.create(pl.Table(position='htbp')) as table:
        table.append(pl.Command('centering'))
        table.append(pl.NoEscape(rel.df_min_tax_obes.to_latex(float_format="%.2f",escape=True,index=False)))
        table.add_caption('Menor aumento no período completo')
doc.append(pl.NewPage())
with doc.create(pl.Subsection('Brasil')):
    doc.append(pl.NoEscape(rel.text_brazil_obes1))
    with doc.create(pl.Figure(position='htbp')) as figure5:
        figure5.add_image('img/figure6.png', width='280px')
        figure5.add_caption('Ordenamento da Taxa de Crescimento do Indíce de Obesidade')  
    doc.append(pl.NoEscape(rel.text_brazil_obes2))    
    with doc.create(pl.Figure(position='htbp')) as figure5:
        figure5.add_image('img/figure7.png', width='450px')
        figure5.add_caption('Ordenamento do Indíce de Obesidade')
doc.append(pl.NewPage())
with doc.create(pl.Section('GDP')):
    with doc.create(pl.Subsection('Crescimento de PIB entre Regiões')):
        with doc.create(pl.Figure(position='htbp')) as figure1:
            figure1.add_image('img/figure1.png', width='280px')
            figure1.add_caption('Regiões de maiores crescimentos de PIB')
        with doc.create(pl.Table(position='htbp')) as table:
            countries = rel.max_pib.drop(columns=['Year','year','GDP_pp','GDP_pp_diff']).head(5)
            table.append(pl.Command('centering'))
            table.append(pl.NoEscape(countries.to_latex(float_format="%.2f",escape=True,index=False)))
            table.add_caption('Países de maiores crescimentos de PIB')
doc.append(pl.NewPage())
with doc.create(pl.Section('Relações')):
    with doc.create(pl.Subsection('PIB e Obesidade')):
        doc.append(pl.NoEscape(rel.text_relations))
        with doc.create(pl.Figure(position='htbp')) as figure2:
            figure2.add_image('img/figure2.png', width='280px')
            figure2.add_caption('Países com Maior "Obesity"')
        with doc.create(pl.Figure(position='htbp')) as figure3:
            figure3.add_image('img/figure3.png', width='280px')
            figure3.add_caption('Países com Maior "GDP_pp"')
doc.append(pl.NewPage())
with doc.create(pl.Subsection('EUA, Brasil e Portugal')):
    doc.append(pl.NoEscape(rel.text_brazil))
    with doc.create(pl.Figure(position='htbp')) as figure4:
        figure4.add_image('img/figure4.png', width='280px')
        figure4.add_caption('Ordenamento por "Obesity"')
    with doc.create(pl.Figure(position='htbp')) as figure5:
        figure5.add_image('img/figure5.png', width='280px')
        figure5.add_caption('Ordenamento por "GDP_pp"')




# doc.generate_tex('tex/relatorio')
doc.generate_pdf('relatorio',compiler='C:/Users/joao44379/AppData/Local/Programs/MiKTeX/miktex/bin/x64/miktex-texworks.exe')
# doc.generate_pdf('report',compiler='C:/Users/joao44379/AppData/Local/Programs/MiKTeX/miktex/bin/x64/miktex-console.exe')