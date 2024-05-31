import pandas as pd
from datetime import datetime
import numpy as np

def export_csv(dataframe, path_file,dataframe_file_name):
    dataframe.to_csv(path_file+dataframe_file_name+'.csv', index=False)
    print('DataFrame Exportado')

df = pd.DataFrame()
df2 = pd.DataFrame()
obesidade_bruto = pd.read_csv("Obesity/obseity-brute.csv")
obesidade_tratado = obesidade_bruto.rename(columns={'Unnamed: 0':'Country'})
obesidade_tratado = obesidade_tratado.drop(0)
obesidade_tratado = obesidade_tratado.drop(1)
# print(obesidade_tratado.head())
# print(obesidade_tratado.columns)

colunas = obesidade_tratado.drop('Country',axis=1).columns
paises = obesidade_tratado['Country'].to_list()


for c in colunas:
    df_melted = pd.melt(obesidade_tratado, value_vars=[c], var_name='Year.X', value_name='Obesity (%)')
    year = c.split('.')[0]
    df_melted.insert(0, 'Country', paises)
    df_melted.insert(1, 'Year', year)
    sex = df_melted.loc[0,'Obesity (%)']
    df_melted['Sex'] = sex
    df_melted = df_melted.drop(0)
    df_melted = df_melted.drop('Year.X',axis=1)
    df_melted = df_melted.sort_values(by=['Country', 'Year'])
    df = pd.concat([df, df_melted], ignore_index=True)

for c in colunas:
    df_melted = pd.melt(obesidade_tratado, value_vars=[c], var_name='Year.X', value_name='Obesity')
    year = c.split('.')[0]
    df_melted.insert(0, 'Country', paises)
    df_melted.insert(1, 'Year', year)
    sex = df_melted.loc[0,'Obesity']
    df_melted['Sex'] = sex
    df_melted = df_melted.drop(0)
    df_melted = df_melted.drop('Year.X',axis=1)
    df_melted[['Obesity_Value (%)', 'Obesity_Min (%)', 'Obesity_Max (%)']] = df_melted['Obesity'].str.extract(r'([\d.]+)\s*\[\s*([\d.]+)-([\d.]+)\s*\]')
    df_melted[['Obesity_Value (%)', 'Obesity_Min (%)', 'Obesity_Max (%)']] = df_melted[['Obesity_Value (%)', 'Obesity_Min (%)', 'Obesity_Max (%)']].astype(float)
    df_melted.drop(columns=['Obesity'], inplace=True)
    df_melted = df_melted.sort_values(by=['Country', 'Year'])
    df2 = pd.concat([df2, df_melted], ignore_index=True)

path_file = 'Obesity/'
df_file_name = f'Unificado-{datetime.now().date()}'
df2_file_name = f'Separado-{datetime.now().date()}'
# export_csv(df2,path_file,df2_file_name)


# Pergunta 1 - Entre homens mulheres são parecidos?
df2_males = df2[df2['Sex'] == 'Male']
males_alt = df2_males.drop('Country',axis=1)
males_alt = males_alt.drop('Sex',axis=1)
males_alt = males_alt.drop('Year',axis=1)


df2_females = df2[df2['Sex'] == 'Female']
females_alt = df2_females.drop('Country',axis=1)
females_alt = females_alt.drop('Sex',axis=1)
females_alt = females_alt.drop('Year',axis=1)


# print('\n\nDescrição - Homens')
# print(males_alt.describe())
# print('\nDescrição - Mulheres')
# print(females_alt.describe())

# Pergunta 2 - Percentual médio de obesidade por sexo na américa do norte no ano de 2010
countries = ['United States of America', 'Canada', 'Mexico']
columns_drop = ['Country', 'Year', 'Sex']
df2_both_2010_nort = df2[(df2['Sex'] == 'Both sexes') & (df2['Year'] == '2010') & (df2['Country'].isin(countries))].drop(columns=columns_drop)
df2_males_2010_nort = df2[(df2['Sex'] == 'Male') & (df2['Year'] == '2010') & (df2['Country'].isin(countries))].drop(columns=columns_drop)
df2_females_2010_nort = df2[(df2['Sex'] == 'Female') & (df2['Year'] == '2010') & (df2['Country'].isin(countries))].drop(columns=columns_drop)


# print('Percentual médio de obesidade por sexo na américa do norte no ano de 2010')
# print(f'Both Sexes - {df2_both_2010_nort.mean()['Obesity_Value (%)']}')
# print(f'Males - {df2_males_2010_nort.mean()['Obesity_Value (%)']}')
# print(f'Females - {df2_females_2010_nort.mean()['Obesity_Value (%)']}')

# Pergunta 3 - Top 3 com maior e menor taxa de aumento de índices de obesidade nesse período de 2010? E em 2016?
# Tentativa 1
df2_both_2010 = df2[(df2['Sex'] == 'Both sexes') & (df2['Year'] == '2010')].sort_values(by=['Obesity_Value (%)'],  ascending=False)
df2_males_2010 = df2[(df2['Sex'] == 'Male') & (df2['Year'] == '2010')].sort_values(by=['Obesity_Value (%)'],  ascending=False)
df2_females_2010 = df2[(df2['Sex'] == 'Female') & (df2['Year'] == '2010')].sort_values(by=['Obesity_Value (%)'],  ascending=False)

df2_both_2016 = df2[(df2['Sex'] == 'Both sexes') & (df2['Year'] == '2016')].sort_values(by=['Obesity_Value (%)'],  ascending=False)
df2_males_2016 = df2[(df2['Sex'] == 'Male') & (df2['Year'] == '2016')].sort_values(by=['Obesity_Value (%)'],  ascending=False)
df2_females_2016 = df2[(df2['Sex'] == 'Female') & (df2['Year'] == '2016')].sort_values(by=['Obesity_Value (%)'],  ascending=False)

# print('Top 3 - 2010')
# print(df2_both_2010.head())

# print('\n\nTop 3 - 2016')
# print(df2_both_2016.head())


# Tentativa 2
df2_both_2010_two = df2[(df2['Sex'] == 'Both sexes') & (df2['Year'].isin(['2009','2010']))].sort_values(by=['Country', 'Year'])
df2_both_2010_two['Tax_Obesity_Value (%)'] = df2_both_2010_two.groupby('Country')['Obesity_Value (%)'].diff()
df2_both_2010_with_tax = df2_both_2010_two[df2_both_2010_two['Year'] == '2010'].sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)


df2_both_2016_two = df2[(df2['Sex'] == 'Both sexes') & (df2['Year'].isin(['2015','2016']))].sort_values(by=['Country', 'Year'])
df2_both_2016_two['Tax_Obesity_Value (%)'] = df2_both_2016_two.groupby('Country')['Obesity_Value (%)'].diff()
df2_both_2016_with_tax = df2_both_2016_two[df2_both_2016_two['Year'] == '2016'].sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)

# print('Top 3 - 2010')
# print(df2_both_2010_with_tax.head())
# print('\n\nTop 3 - 2016')
# print(df2_both_2016_with_tax.head())

# Pergunta 4 - Top 3 com maior e menor taxa de aumento de índices de obesidade no período completo
df2_both = df2[df2['Sex'] == 'Both sexes'].sort_values(by=['Country', 'Year'])
df2_both['Tax_Obesity_Value (%)'] = df2_both.groupby('Country')['Obesity_Value (%)'].diff()
df2_both_with_tax = df2_both.sort_values(by=['Tax_Obesity_Value (%)'],  ascending=False)

print(df2_both_with_tax)