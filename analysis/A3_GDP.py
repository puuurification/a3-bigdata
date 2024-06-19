import pandas as pd

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

# Cria um DataFrame completo de anos usando a menor e a maior data como range para a interpolação
years = pd.DataFrame({'Year': pd.date_range(start=df['Year'].min(), end=df['Year'].max(), freq='AS')})

# Converter para str as duas colunas que serão usadas como conexão no merge
years = years.astype(str)
df['Year'] = df['Year'].astype(str)

# Função para interpolar dados para cada país
def interpolate_country_data(country_df):
    # Merge entre o DataFrame de anos completos com os dados do país
    country_df = years.merge(country_df, on='Year', how='left')
    # Interpola os valores de PIB per capita
    country_df['GDP_pp'] = country_df['GDP_pp'].interpolate()
    # completa espaços nulos
    country_df = country_df.ffill(axis = 0)
    
    return country_df


# Aplica a função de interpolação para cada país e região
interpolated_df = df.groupby(['Country', 'Region']).apply(interpolate_country_data).reset_index(drop=True)

# Isolando o ano no registro da data
interpolated_df['temp_year'] = pd.to_datetime(interpolated_df['Year']) 
interpolated_df['Year'] = interpolated_df['temp_year'].dt.year
interpolated_df.drop(columns=['temp_year'], inplace=True)
print(interpolated_df)

# Salva o DataFrame interpolado em um novo arquivo CSV
# interpolated_df.to_csv("Interpolated_GDP_pp.csv", index=False)
