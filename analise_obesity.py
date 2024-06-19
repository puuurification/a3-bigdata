import pandas as pd
import plotly.express as px

# Carrega o arquivo CSV
df = pd.read_csv("data/obesity-brute.csv", header=[0,3])

# Mudar o index do Dataframe pelo de Country
newdf = df.set_index(("Unnamed: 0_level_0"))

# Remodelar o DataFrame fornecido transpondo o nível de coluna especificado para o nível de linha.
df_object = newdf.stack([0,1],future_stack=True).swaplevel(0)

# Convertendo objeto em dataframe
df_formated = df_object.to_frame().reset_index()

# Mudando o nome das colunas
df_formated.rename(columns={
    "level_0": "Sex",
    "level_1": "year",
    "Unnamed: 0_level_0": "Country",
    0: "Obesity_percentual"
}, inplace=True)

# Convertendo elemnetos tuples em linhas
df_formated = df_formated.explode("Country")

# new data frame with split value columns
new = df_formated["Obesity_percentual"].str.split(" ", n=1, expand=True)
 
# making separate first name column from new data frame
df_formated["Obesity"] = new[0]

# Converter coluna Obesity em tipo numerico e os valores não numericos em NaN
df_formated['Obesity'] = df_formated['Obesity'].apply(pd.to_numeric, errors='coerce')

# Deletar linhas com coluna Obesity NaN
df_formated.dropna(inplace=True)

# Ordenar dados por pais e ano
df_formated = df_formated.sort_values(by=['Country','year'])

# Criando nova coluna com a diferença da taxa de obesidade agrupada por pais e sexo
df_formated['obesity_diff'] = df_formated.groupby(['Country','Sex'])['Obesity'].diff().fillna(0)

df_formated['obesity_cumsum_diff'] = df_formated.groupby(['Country','Sex'])['obesity_diff'].cumsum()

# Salva o DataFrame formatado
df_formated.to_csv("data/obesity-cleaned.csv", index=False)