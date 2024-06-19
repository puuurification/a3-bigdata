import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df_gdp = pd.read_csv('data/GDP_interpolated.csv')
df_obesity = pd.read_csv('data/obesity-cleaned.csv')


max_year = df_gdp.year.max()
df_last_year = df_gdp[df_gdp['year'] == max_year].sort_values(by=['GDP_pp_cumsum_diff'], ascending=False)
max_pib = df_last_year.copy()
regions = df_gdp.groupby(['Region'])['GDP_pp_cumsum_diff'].sum().reset_index()
regions = regions.sort_values(by=['GDP_pp_cumsum_diff'], ascending=False)
# print(regions.sort_values(by=['GDP_pp_cumsum_diff'], ascending=False))
# print(regions)


# print("Regiões de maiores crescimentos de PIB")
# print(df_last_year.head(5),'\n')

# print("Regiões de menores crescimentos de PIB")
# print(df_last_year.tail(5),'\n')

fig = px.bar(df_last_year.head(5), x='Country', y="GDP_pp_cumsum_diff", title="Regiões de maiores crescimentos de PIB")
# fig.show()

fig = px.bar(df_last_year.tail(5), x='Country', y="GDP_pp_cumsum_diff", title="Regiões de menores crescimentos de PIB")
# fig.show()

###########################################################################################################################
###########################################################################################################################

indexs = ['Média','Desvio Padrão','Mínimo','Máximo']
df_union_describe_sexes = pd.DataFrame({
    'Homens': [df_obesity[df_obesity['Sex'] == 'Male'].describe(include='all')['Obesity'].loc['mean'],
               df_obesity[df_obesity['Sex'] == 'Male'].describe(include='all')['Obesity'].loc['std'],
               df_obesity[df_obesity['Sex'] == 'Male'].describe(include='all')['Obesity'].loc['min'],
               df_obesity[df_obesity['Sex'] == 'Male'].describe(include='all')['Obesity'].loc['max']], 
    'Mulheres': [df_obesity[df_obesity['Sex'] == 'Female'].describe(include='all')['Obesity'].loc['mean'],
               df_obesity[df_obesity['Sex'] == 'Female'].describe(include='all')['Obesity'].loc['std'],
               df_obesity[df_obesity['Sex'] == 'Female'].describe(include='all')['Obesity'].loc['min'],
               df_obesity[df_obesity['Sex'] == 'Female'].describe(include='all')['Obesity'].loc['max']]
    },index=indexs)

union_describe_sexes = '''
As mulheres apresentam uma média de obesidade mais alta (15.53\%) 
comparada aos homens (9.33\%). Além disso, a distribuição das 
porcentagens de obesidade é mais ampla entre as mulheres, como 
indicado pelo maior desvio padrão e valores máximos mais altos. 
'''

# Lista com os países da America do Norte
north_america_countries = ["United States of America", "Mexico", "Canada"]

# Filtro para paises da America do Norte
df_north_america = df_obesity[df_obesity['Country'].isin(north_america_countries)]

# Calculo da media de obesidade agrupado por ano e sexo
df_north_america_mean = df_north_america.groupby(['year','Sex'])['Obesity'].mean().reset_index()

# print("Percentual médio de obesidade por sexo na américa do norte no ano de 2010")
# print(df_north_america_mean[df_north_america_mean['year'] == 2010],'\n')
df_north_america_mean_2010 = df_north_america_mean[df_north_america_mean['year'] == 2010]

# print("Top 3 com menor taxa de aumento de índices de obesidade 2016")
q3_drop = ['Obesity_percentual','year','obesity_cumsum_diff']
df_min_tax_obes_2016 = df_obesity[df_obesity['year']==2016].sort_values(['Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).tail(3)
df_min_tax_obes_2016.drop(columns=q3_drop,inplace=True)
# print(df_obesity[df_obesity['year']==2016].sort_values(['Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).tail(3),'\n')
# print(df_min_tax_obes_2016)

# print("Top 3 com maior taxa de aumento de índices de obesidade 2016")
df_max_tax_obes_2016 = df_obesity[df_obesity['year']==2016].sort_values(['Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).head(3)
df_max_tax_obes_2016.drop(columns=q3_drop,inplace=True)
# print(df_obesity[df_obesity['year']==2016].sort_values(['Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).head(3),'\n')
# print(df_max_tax_obes_2016)


# print("Top 3 com menor taxa de aumento de índices de obesidade 2010")
df_min_tax_obes_2010 = df_obesity[df_obesity['year']==2010].sort_values(['Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).tail(3)
df_min_tax_obes_2010.drop(columns=q3_drop,inplace=True)
# print(df_obesity[df_obesity['year']==2010].sort_values(['Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).tail(3),'\n')
# print(df_min_tax_obes_2010)

# print("Top 3 com maior taxa de aumento de índices de obesidade 2010")
df_max_tax_obes_2010 = df_obesity[df_obesity['year']==2010].sort_values(['Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).head(3)
df_max_tax_obes_2010.drop(columns=q3_drop,inplace=True)
# print(df_obesity[df_obesity['year']==2010].sort_values(['Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).head(3),'\n')
# print(df_max_tax_obes_2010)


max_year = df_obesity.year.max()
q4_drop = ['Obesity_percentual','year','obesity_diff','Obesity']
# print("Top 3 com menor taxa de aumento de índices de obesidade no período completo")
df_min_tax_obes = df_obesity[df_obesity['year']==max_year].sort_values(['Sex','obesity_cumsum_diff'],ascending=False).groupby(['Sex','year']).tail(3)
df_min_tax_obes.drop(columns=q4_drop,inplace=True)
# print(df_obesity[df_obesity['year']==max_year].sort_values(['Sex','obesity_cumsum_diff'],ascending=False).groupby(['Sex','year']).tail(3),'\n')

# print("Top 3 com maior taxa de aumento de índices de obesidade no período completo")
df_max_tax_obes = df_obesity[df_obesity['year']==max_year].sort_values(['Sex','obesity_cumsum_diff'],ascending=False).groupby(['Sex','year']).head(3)
df_max_tax_obes.drop(columns=q4_drop,inplace=True)
# print(df_obesity[df_obesity['year']==max_year].sort_values(['Sex','obesity_cumsum_diff'],ascending=False).groupby(['Sex','year']).head(3),'\n')

df_brazil = df_obesity[df_obesity['Country'] == 'Brazil']
# print(df_brazil.sort_values(['Obesity'],ascending=False))
# print(df_brazil.describe())

fig = px.bar(df_obesity[df_obesity['year'].isin([2010,2016])].sort_values(['year','Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).head(5), x="Country", y="obesity_diff", color='year', facet_row="Sex", facet_col="year",title='Top 5 com maior taxa de aumento de índices de obesidade 2010 e 2016')
# fig.show()


fig = px.bar(df_obesity[df_obesity['year'].isin([2010,2016])].sort_values(['year','Sex','obesity_diff'],ascending=False).groupby(['Sex','year']).tail(5), x="Country", y="obesity_diff", color='year', facet_row="Sex", facet_col="year",title='Top 5 com menor taxa de aumento de índices de obesidade 2010 e 2016')
# fig.show()

max_year = df_obesity.year.max()
df_last_year = df_obesity[df_obesity['year'] == max_year].sort_values(by=['obesity_cumsum_diff'], ascending=False)


fig = px.bar(df_last_year[df_last_year.Sex == 'Female'].head(5), x='Country', y="obesity_cumsum_diff", title="Maior taxa de aumento de índices de obesidade feminino no período completo")
# fig.show()

fig = px.bar(df_last_year[df_last_year.Sex == 'Male'].head(5), x='Country', y="obesity_cumsum_diff", title="Maior taxa de aumento de índices de obesidade masculino no período completo")
# fig.show()

fig = px.bar(df_last_year[df_last_year.Sex == 'Both sexes'].head(5), x='Country', y="obesity_cumsum_diff", title="Maior taxa de aumento de índices de obesidade ambos os sexos no período completo")
# fig.show()

fig = px.bar(df_last_year[df_last_year.Sex == 'Female'].tail(5), x='Country', y="obesity_cumsum_diff", title="Menor taxa de aumento de índices de obesidade feminino no período completo")
# fig.show()

fig = px.bar(df_last_year[df_last_year.Sex == 'Male'].tail(5), x='Country', y="obesity_cumsum_diff", title="Menor taxa de aumento de índices de obesidade masculino no período completo")
# fig.show()

fig = px.bar(df_last_year[df_last_year.Sex == 'Both sexes'].tail(5), x='Country', y="obesity_cumsum_diff", title="Menor taxa de aumento de índices de obesidade ambos os sexos no período completo")
# fig.show()

text_brazil_obes1 = '''
O Brasil é o 3º país da América do Sul em relação ao total de crescimento do indíce de obesidade.
'''

text_brazil_obes2 = '''
Entretanto, no indíce de obesidade, o Brasil encontra-se na 7ª posição dentro da América do Sul.
'''

text_relations = '''
PIB não tem relação direta com o percentual de obesidade, pois como a Figura 4 apresenta, os países com maior indice de obesidade, Nauru e Palau, apresentam PIB 10 vezes menor que os com maiores PIB, Quatar e Luxembourg.
'''

text_brazil = '''
O mesmo permance para o Brasil, em relação aos EUA e Portugal, pois o índice de obesidade do Brasil é superior ao de Portugal e não se encontra com a mesma proporsão que entre obesidade e PIB que EUA e Portugal apresentam.
'''