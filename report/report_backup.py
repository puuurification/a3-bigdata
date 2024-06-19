import numpy as np
import pylatex as pl
import pandas as pd

brute = pd.read_csv("Obesity/obseity-brute.csv", header=[0,3])
new_brute = brute.set_index(("Unnamed: 0_level_0"))
brute_object = new_brute.stack([0,1],future_stack=True).swaplevel(0)
df_formated = brute_object.to_frame().reset_index()
df_formated.rename(columns={
    "level_0": "Sexes",
    "level_1": "Year",
    "Unnamed: 0_level_0": "Country",
    0: "Obesity"
}, inplace=True)
df_formated = df_formated.explode("Country")
obseity = df_formated.copy()
obseity[['Obesity_Value (%)', 'Obesity_Min (%)', 'Obesity_Max (%)']] = df_formated['Obesity'].str.extract(r'([\d.]+)\s*\[\s*([\d.]+)-([\d.]+)\s*\]').astype(float)
obseity.drop('Obesity',axis=1, inplace=True)
df_apart_males = obseity[obseity['Sexes'] == 'Male']
males_alt = df_apart_males['Obesity_Value (%)']
# print(males_alt.describe())
mean = males_alt.describe(include='all').loc['mean']
print(males_alt.describe())
# print(mean)

doc = pl.Document()
doc.preamble.append(pl.Command('title', 'Relatório de Dados - GDP e Obesidade'))
doc.preamble.append(pl.Command('author', 'Rafael Rodrigues, João Purificaçao'))
doc.preamble.append(pl.Command('date', pl.NoEscape(r'\today')))
doc.append(pl.NoEscape(r'\maketitle'))


with doc.create(pl.Section('Resposta')):
    with doc.create(pl.Subsection('Obesidade')):
        with doc.create(pl.Subsubsection('Comparação entre Homens e Mulheres:')):
            with doc.create(pl.Subsubsection('Dados - Homens:')):
                with doc.create(pl.Description()) as desc:
                    desc.add_item("Média:", f'{round(males_alt.describe(include='all').loc['mean'],2)}')
                    desc.add_item("Second", "The second item")
                    desc.add_item("Third", pl.NoEscape("The third etc \\ldots"))
                # doc.append(f'Média:{round(males_alt.describe(include='all').loc['mean'],2)}')
            with doc.create(pl.Subsubsection('Dados - Mulheres:')):
                doc.append('Mulheres')
                doc.append(f'Média:{round(males_alt.describe(include='all').loc['mean'],2)}')
    with doc.create(pl.Subsection('GDP')):
        with doc.create(pl.Subsubsection('Dados')):
            doc.append('Also some crazy characters: $&#{}')




doc.generate_tex('report/tex/report')