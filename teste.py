import pandas as pd

# Criando um DataFrame de exemplo
data = {
    'Country': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'Year': [1980, 1985, 1990, 1995, 2000, 1980, 1985, 1990, 1995, 2000],
    'GDP_pp': [1000, None, 3000, None, 5000, 2000, None, 4000, None, 6000]
}

df = pd.DataFrame(data)

# Exibindo o DataFrame original
print("DataFrame original:")
print(df)

# Interpolando os valores de GDP_pp para cada país
df['GDP_pp'] = df.groupby('Country')['GDP_pp'].apply(lambda group: group.interpolate(method='linear'))

# Exibindo o DataFrame após a interpolação
print("\nDataFrame após a interpolação de GDP_pp:")
print(df)
