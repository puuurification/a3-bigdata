import pandas as pd

# Carrega o arquivo CSV
df = pd.read_csv("data/obseity-brute.csv", header=[0,3])

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
obesity = df_apart.copy()
# print(df_formated)
# print(df_apart)
sexes = ['Both sexes','Male','Female']

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

indexs = 'Média-Desvio Padrão-Mínimo-Máximo'
relaction_mf = pd.DataFrame({
    'Homens': [males_alt.describe(include='all').loc['mean'],males_alt.describe(include='all').loc['std'],males_alt.describe(include='all').loc['min'],males_alt.describe(include='all').loc['max']], 
    'Mulheres': [females_alt.describe(include='all').loc['mean'],females_alt.describe(include='all').loc['std'],females_alt.describe(include='all').loc['min'],females_alt.describe(include='all').loc['max']]
    },index=indexs.split('-'))


# print('\n\nDescrição - Homens')
# print(males_alt.describe())
# print('\nDescrição - Mulheres')
# print(females_alt.describe())

# Pergunta 2 - Percentual médio de obesidade por sexo na américa do norte no ano de 2010
countries = ['Canada', 'Mexico','United States of America']
columns_drop = [ 'Country','Year', 'Sexes']
df_apart_both_2010 = df_apart[(df_apart['Year'] == '2010') & (df_apart['Country'].isin(countries))]
df_apart_both_2010_nort = df_apart[(df_apart['Sexes'] == 'Both sexes') & (df_apart['Year'] == '2010') & (df_apart['Country'].isin(countries))].drop(columns=columns_drop)
df_apart_males_2010_nort = df_apart[(df_apart['Sexes'] == 'Male') & (df_apart['Year'] == '2010') & (df_apart['Country'].isin(countries))].drop(columns=columns_drop)
df_apart_females_2010_nort = df_apart[(df_apart['Sexes'] == 'Female') & (df_apart['Year'] == '2010') & (df_apart['Country'].isin(countries))].drop(columns=columns_drop)
nort_2010 = df_apart_both_2010[['Obesity_Value (%)','Country','Sexes']].set_index('Country')
nort_2010.index.name = None
nort_2010 = nort_2010.sort_values('Sexes')
# nort_2010_both = nort_2010[nort_2010['Sexes']=='Both sexes'].drop(columns='Sexes')
# print(df_apart_both_2010)
# print(df_apart_both_2010_nort)
# print(fgj)
# print(nort_2010.sort_values('Sexes'))

mean_nort_2010 = pd.DataFrame({
    'Obesity_Value (%)': [df_apart_both_2010_nort.mean()['Obesity_Value (%)'],df_apart_males_2010_nort.mean()['Obesity_Value (%)'],df_apart_females_2010_nort.mean()['Obesity_Value (%)']]
}, index=['Both Sexes','Males','Females'])

# print(mean_nort_2010)

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
max_tax_2010 = pd.DataFrame()
max_tax_2016 = pd.DataFrame()
min_tax_2010 = pd.DataFrame()
min_tax_2016 = pd.DataFrame()
max_tax_all = pd.DataFrame()
min_tax_all = pd.DataFrame()
for sex in sexes:
    # Pergunta 3 - Top 3 com maior e menor taxa de aumento de índices de obesidade nesse período de 2010? E em 2016?
    df_apart_both_2010_two = df_apart[(df_apart['Sexes'] == sex) & (df_apart['Year'].isin(['2009','2010']))].sort_values(by=['Country', 'Year'])
    df_apart_both_2010_two['Tax_Obesity_Value (%)'] = df_apart_both_2010_two.groupby('Country')['Obesity_Value (%)'].diff()
    df_apart_both_2010_with_tax = df_apart_both_2010_two[df_apart_both_2010_two['Year'] == '2010'].sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
    max_tax_2010 = pd.concat([max_tax_2010, df_apart_both_2010_with_tax.head(3)],axis=0,ignore_index=True)
    min_tax_2010 = pd.concat([min_tax_2010, df_apart_both_2010_with_tax.dropna().tail(3)],axis=0,ignore_index=True)

    df_apart_both_2016_two = df_apart[(df_apart['Sexes'] == sex) & (df_apart['Year'].isin(['2015','2016']))].sort_values(by=['Country', 'Year'])
    df_apart_both_2016_two['Tax_Obesity_Value (%)'] = df_apart_both_2016_two.groupby('Country')['Obesity_Value (%)'].diff()
    df_apart_both_2016_with_tax = df_apart_both_2016_two[df_apart_both_2016_two['Year'] == '2016'].sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
    max_tax_2016 = pd.concat([max_tax_2016, df_apart_both_2016_with_tax.head(3)],axis=0,ignore_index=True)
    min_tax_2016 = pd.concat([min_tax_2016, df_apart_both_2016_with_tax.dropna().tail(3)],axis=0,ignore_index=True)

    # Pergunta 4 - Top 3 com maior e menor taxa de aumento de índices de obesidade no período completo
    df_apart_both = df_apart[df_apart['Sexes'] == sex].sort_values(by=['Country', 'Year'])
    df_apart_both['Tax_Obesity_Value (%)'] = df_apart_both.groupby('Country')['Obesity_Value (%)'].diff()
    df_apart_both_with_tax = df_apart_both.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
    max_tax_all = pd.concat([max_tax_all, df_apart_both_with_tax.head(3)],axis=0,ignore_index=True)
    min_tax_all = pd.concat([min_tax_all, df_apart_both_with_tax.dropna().tail(3)],axis=0,ignore_index=True)
    

tax_columns = ['Obesity_Value (%)','Year','Obesity_Min (%)','Obesity_Max (%)']
max_tax_2010 = max_tax_2010.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
max_tax_2010.drop(columns=tax_columns, inplace=True)

max_tax_2016 = max_tax_2016.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
max_tax_2016.drop(columns=tax_columns, inplace=True)

min_tax_2010 = min_tax_2010.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
min_tax_2010.drop(columns=tax_columns, inplace=True)

min_tax_2016 = min_tax_2016.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
min_tax_2016.drop(columns=tax_columns, inplace=True)

max_tax_all = max_tax_all.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
max_tax_all.drop(columns=['Obesity_Value (%)','Obesity_Min (%)','Obesity_Max (%)'], inplace=True)

min_tax_all = min_tax_all.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=True)
min_tax_all.drop(columns=['Obesity_Value (%)','Obesity_Min (%)','Obesity_Max (%)'], inplace=True)

print(min_tax_all)






# print('Top 3 - 2010')
# print(df_apart_both_2010_with_tax.head(3))
# print(df_apart_both_2010_with_tax.dropna().tail())
# print('\n\nTop 3 - 2016')
# print(df_apart_both_2016_with_tax.head())

# Pergunta 4 - Top 3 com maior e menor taxa de aumento de índices de obesidade no período completo
df_apart_both = df_apart[df_apart['Sexes'] == 'Both sexes'].sort_values(by=['Country', 'Year'])
df_apart_both['Tax_Obesity_Value (%)'] = df_apart_both.groupby('Country')['Obesity_Value (%)'].diff()
# df_apart_both.fillna(0, inplace=True)
df_apart_both_with_tax = df_apart_both.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)
# df_apart_both_with_tax = df_apart_both.sort_values(by=['Country', 'Year'],  ascending=True)

print(df_apart_both_with_tax.dropna())
# print(df_apart_both_with_tax[df_apart_both_with_tax['Country']=='Sudan (former)'])