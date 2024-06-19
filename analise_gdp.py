import pandas as pd
import plotly.express as px

# Carrega o arquivo CSV
df = pd.read_csv("data/GDP.xls")

# Limpa espaços vazios no nome das colunas
df.columns = df.columns.str.strip()

# seleciona quais colunas são do tipo object
object_columns = df.select_dtypes(include=['object']).columns

# Limpa os espaços vazios que possam existir nas colunas do tipo object
for item in object_columns:
    df[item] = df[item].str.strip()

# Retira a virgula do numeros e depois faz a conversão para float
df['GDP_pp'] = df['GDP_pp'].apply(lambda x: float(x.replace(',', '')))

# Converte a coluna 'Year' para datetime e extrai a data
df['Year'] = pd.to_datetime(df['Year']).dt.date

# Função para interpolar dados para cada país
def interpolate_country_data(df_country):
    # Cria um DataFrame completo de anos usando a menor e a maior data como range para a interpolação
    years = pd.DataFrame({'Year': pd.date_range(start=df_country['Year'].min(), end=df_country['Year'].max(), freq='YS')})

    # Converter para datetime as duas colunas que serão usadas como conexão no merge
    years['Year'] = pd.to_datetime(years['Year'])
    df_country['Year'] = pd.to_datetime(df_country['Year'])
    
    # Merge entre o DataFrame de anos completos com os dados do país
    df_country = years.merge(df_country, on='Year', how='left')
    
    # Interpola os valores de PIB per capita
    df_country['GDP_pp'] = df_country['GDP_pp'].interpolate()
    
    # completa espaços nulos
    df_country = df_country.ffill(axis = 0)
    
    return df_country

# Aplica a função de interpolação para cada país e região
df_interpolated = df.groupby(['Country', 'Region'])[df.columns].apply(interpolate_country_data).reset_index(drop=True)

# Converte a coluna 'Year' para datetime e extrai o ano
df_interpolated['year'] = pd.to_datetime(df_interpolated['Year']).dt.year.astype('int64')

df_interpolated = df_interpolated.sort_values(by=['Country', 'Year'])

df_interpolated['GDP_pp_diff'] = df_interpolated.groupby(['Country'])['GDP_pp'].diff().fillna(0)

df_interpolated['GDP_pp_cumsum_diff'] = df_interpolated.groupby(['Country'])['GDP_pp_diff'].cumsum()

# Salva o DataFrame interpolado em um novo arquivo CSV
df_interpolated.to_csv("data/GDP_interpolated.csv", index=False)