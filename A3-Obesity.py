import pandas as pd

# Carrega o arquivo CSV
df = pd.read_csv("Obesity/obseity-brute.csv", header=[0,3])

# Mudar o index do Dataframe pelo de Country
newdf = df.set_index(("Unnamed: 0_level_0"))

# Remodelar o DataFrame fornecido transpondo o nível de coluna especificado para o nível de linha.
df_object = newdf.stack([0,1],future_stack=True).swaplevel(0)

# Convertendo objeto em dataframe
df_formated = df_object.to_frame().reset_index()

# Mudando o nome das colunas
df_formated.rename(columns={
    "level_0": "Sexes",
    "level_1": "Year",
    "Unnamed: 0_level_0": "Country",
    0: "Obesity"
}, inplace=True)

# Convertendo elemnetos tuples em linhas
df_formated = df_formated.explode("Country")

# Salva o DataFrame formatado
# df_formated.to_csv("obesity.csv", index=False)

df_apart = df_formated.copy()
df_apart[['Obesity_Value (%)', 'Obesity_Min (%)', 'Obesity_Max (%)']] = df_formated['Obesity'].str.extract(r'([\d.]+)\s*\[\s*([\d.]+)-([\d.]+)\s*\]').astype(float)
df_apart.drop('Obesity',axis=1, inplace=True)
# print(df_formated)
# print(df_apart)

# Pergunta 1 - Entre homens mulheres são parecidos?
df_apart_males = df_apart[df_apart['Sexes'] == 'Male']
males_alt = df_apart_males['Obesity_Value (%)']
# males_alt = df_apart_males.drop('Country',axis=1)
# males_alt = males_alt.drop('Sexes',axis=1)
# males_alt = males_alt.drop('Year',axis=1)
# print(males_alt)


df_apart_females = df_apart[df_apart['Sexes'] == 'Female']
females_alt = df_apart_females['Obesity_Value (%)']
# females_alt = df_apart_females.drop('Country',axis=1)
# females_alt = females_alt.drop('Sexes',axis=1)
# females_alt = females_alt.drop('Year',axis=1)
# print(females_alt)


# print('\n\nDescrição - Homens')
# print(males_alt.describe())
# print('\nDescrição - Mulheres')
# print(females_alt.describe())

# Pergunta 2 - Percentual médio de obesidade por sexo na américa do norte no ano de 2010
countries = ['United States of America', 'Canada', 'Mexico']
columns_drop = ['Country', 'Year', 'Sexes']
df_apart_both_2010_nort = df_apart[(df_apart['Sexes'] == 'Both sexes') & (df_apart['Year'] == '2010') & (df_apart['Country'].isin(countries))].drop(columns=columns_drop)
df_apart_males_2010_nort = df_apart[(df_apart['Sexes'] == 'Male') & (df_apart['Year'] == '2010') & (df_apart['Country'].isin(countries))].drop(columns=columns_drop)
df_apart_females_2010_nort = df_apart[(df_apart['Sexes'] == 'Female') & (df_apart['Year'] == '2010') & (df_apart['Country'].isin(countries))].drop(columns=columns_drop)
# print(df_apart_both_2010_nort)


# print('Percentual médio de obesidade por sexo na américa do norte no ano de 2010')
# print(f'Both Sexes - {df_apart_both_2010_nort.mean()['Obesity_Value (%)']}')
# print(f'Males - {df_apart_males_2010_nort.mean()['Obesity_Value (%)']}')
# print(f'Females - {df_apart_females_2010_nort.mean()['Obesity_Value (%)']}')

# Pergunta 3 - Top 3 com maior e menor taxa de aumento de índices de obesidade nesse período de 2010? E em 2016?
# Tentativa 1
df_apart_both_2010 = df_apart[(df_apart['Sexes'] == 'Both sexes') & (df_apart['Year'] == '2010')].sort_values(by=['Obesity_Value (%)'],  ascending=False)
df_apart_males_2010 = df_apart[(df_apart['Sexes'] == 'Male') & (df_apart['Year'] == '2010')].sort_values(by=['Obesity_Value (%)'],  ascending=False)
df_apart_females_2010 = df_apart[(df_apart['Sexes'] == 'Female') & (df_apart['Year'] == '2010')].sort_values(by=['Obesity_Value (%)'],  ascending=False)

df_apart_both_2016 = df_apart[(df_apart['Sexes'] == 'Both sexes') & (df_apart['Year'] == '2016')].sort_values(by=['Obesity_Value (%)'],  ascending=False)
df_apart_males_2016 = df_apart[(df_apart['Sexes'] == 'Male') & (df_apart['Year'] == '2016')].sort_values(by=['Obesity_Value (%)'],  ascending=False)
df_apart_females_2016 = df_apart[(df_apart['Sexes'] == 'Female') & (df_apart['Year'] == '2016')].sort_values(by=['Obesity_Value (%)'],  ascending=False)

# print('Top 3 - 2010')
# print(df_apart_both_2010.head())

# print('\n\nTop 3 - 2016')
# print(df_apart_both_2016.head())


# Tentativa 2
df_apart_both_2010_two = df_apart[(df_apart['Sexes'] == 'Both sexes') & (df_apart['Year'].isin(['2009','2010']))].sort_values(by=['Country', 'Year'])
df_apart_both_2010_two['Tax_Obesity_Value (%)'] = df_apart_both_2010_two.groupby('Country')['Obesity_Value (%)'].diff()
df_apart_both_2010_with_tax = df_apart_both_2010_two[df_apart_both_2010_two['Year'] == '2010'].sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)


df_apart_both_2016_two = df_apart[(df_apart['Sexes'] == 'Both sexes') & (df_apart['Year'].isin(['2015','2016']))].sort_values(by=['Country', 'Year'])
df_apart_both_2016_two['Tax_Obesity_Value (%)'] = df_apart_both_2016_two.groupby('Country')['Obesity_Value (%)'].diff()
df_apart_both_2016_with_tax = df_apart_both_2016_two[df_apart_both_2016_two['Year'] == '2016'].sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)

# print('Top 3 - 2010')
# print(df_apart_both_2010_with_tax.head())
# print(df_apart_both_2010_with_tax.tail())
# print('\n\nTop 3 - 2016')
# print(df_apart_both_2016_with_tax.head())

# Pergunta 4 - Top 3 com maior e menor taxa de aumento de índices de obesidade no período completo
df_apart_both = df_apart[df_apart['Sexes'] == 'Both sexes'].sort_values(by=['Country', 'Year'])
df_apart_both['Tax_Obesity_Value (%)'] = df_apart_both.groupby('Country')['Obesity_Value (%)'].diff()
# df_apart_both.fillna(0, inplace=True)
df_apart_both_with_tax = df_apart_both.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
# df_apart_both_with_tax = df_apart_both.sort_values(by=['Country', 'Year'],  ascending=True)

# print(df_apart_both_with_tax)
# print(df_apart_both_with_tax[df_apart_both_with_tax['Country']=='Sudan (former)'])