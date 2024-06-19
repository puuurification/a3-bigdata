# %%
import pandas as pd

# Carrega o arquivo CSV
df = pd.read_csv("data.csv", header=[0,3])

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
    0: "Obesity_percentual"
}, inplace=True)

# Convertendo elemnetos tuples em linhas
df_formated = df_formated.explode("Country")
# %%
# Salva o DataFrame formatado
df_formated.to_csv("obesity.csv", index=False)

# new data frame with split value columns
new = df_formated["Obesity_percentual"].str.split(" ", n=1, expand=True)
 
# making separate first name column from new data frame
df_formated["Obesity"] = new[0]

# Converter coluna Obesity em tipo numerico e os valores não numericos em NaN
df_formated['Obesity'] = df_formated['Obesity'].apply(pd.to_numeric, errors='coerce')

# Deletar linhas com coluna Obesity NaN
df_formated.dropna(inplace=True)

# filtro para Obesidade do sexo masculino
df_male = df_formated[df_formated['Sexes'] == 'Male']

# filtro para Obesidade do sexo feminino
df_female = df_formated[df_formated['Sexes'] == 'Female']

print(df_male.describe())

print(df_female.describe())

'''
As mulheres apresentam uma média de obesidade mais alta (15.53%) 
comparada aos homens (9.33%). Além disso, a distribuição das 
porcentagens de obesidade é mais ampla entre as mulheres, como 
indicado pelo maior desvio padrão e valores máximos mais altos. 
'''

# Lista com os países da America do Norte
north_america_countries = ["United States of America", "Mexico", "Canada"]

# Filtro para paises da America do Norte
df_north_america = df_formated[df_formated['Country'].isin(north_america_countries)]

# Calculo da media de obesidade agrupado por ano e sexo
df_north_america_mean = df_north_america.groupby(['Year','Sexes'])['Obesity'].mean().reset_index()

print("Percentual médio de obesidade por sexo na américa do norte no ano de 2010")
print(df_north_america_mean[df_north_america_mean['Year'] == '2010'])

# Media das obesidades por ano e país
df_mean = df_formated.groupby(['Country','Year'])['Obesity'].mean().reset_index()

# Calculo da taxa por ano agrupado por país
df_mean['diff_mean'] = df_mean.groupby('Country')['Obesity'].diff()

# Selecionar os três menores por ano
df_tail=df_mean.sort_values(['diff_mean'],ascending=False).groupby('Year').tail(3)

print("3 menores taxas de aumento de índices de obesidade no período de 2010")
print(df_tail[df_tail['Year'] == '2010'])

print("3 menores taxas de aumento de índices de obesidade no período de 2016")
print(df_tail[df_tail['Year'] == '2016'])

# Selecionar os três maiores por ano
df_head=df_mean.sort_values(['diff_mean'],ascending=False).groupby('Year').head(3)

print("3 maiores taxas de aumento de índices de obesidade no período de 2010")
print(df_head[df_head['Year'] == '2010'])

print("3 maiores taxas de aumento de índices de obesidade no período de 2016")
print(df_head[df_head['Year'] == '2016'])

# Agrupamento por país
df_groupby = df_mean.groupby("Country")

# Selecionando os dados do primeiro e ultimo ano da tabela
df_head_tail = (pd.concat([df_groupby.head(1),df_groupby.tail(1)]).drop_duplicates().sort_values(by=["Country","Year"]).reset_index(drop=True))

# Calculo da taxa entre o primeiro e o ultimo registro
df_head_tail['diff_mean'] = df_head_tail.groupby('Country')['Obesity'].diff()

# Deletar linhas com taxa vazios
df_head_tail.dropna(inplace=True)

# Selecionar os três menores
df_tail2=df_head_tail.sort_values(['diff_mean'],ascending=False).groupby('Year').tail(3)

# Selecionar os três maiores
df_head2=df_head_tail.sort_values(['diff_mean'],ascending=False).groupby('Year').head(3)
