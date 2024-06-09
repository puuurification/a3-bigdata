import pandas as pd
from datetime import datetime
import numpy as np

def export_csv(dataframe, path_file,dataframe_file_name):
    dataframe.to_csv(path_file+dataframe_file_name+'.csv', index=False)
    print('DataFrame Exportado')

def get_gdp_pp(df, country, year):
    filtered_df = df[(df['Country'] == country) & (df['Year'] == year)]
    
    if not filtered_df.empty:
        return filtered_df['GDP_pp'].values[0]
    else:
        return None
    

def get_region(df, country):
    filtered_df = df[(df['Country'] == country)]
    
    if not filtered_df.empty:
        return filtered_df['Region'].values[0]
    else:
        return None


path_file = 'GDP/'
file_path = 'GDP/GDP.xls'

gdp_brute = pd.read_csv("GDP/GDP.xls")
df3 = pd.read_csv("GDP/df3.csv")
df = gdp_brute.copy()

df['temp_year'] = pd.to_datetime(gdp_brute['Year']) 
df['Year'] = df['temp_year'].dt.year
df.drop(columns=['temp_year'], inplace=True)
df.rename(columns={' GDP_pp ': 'GDP_pp'}, inplace=True) #Resolvido
df['GDP_pp'] = df['GDP_pp'].str.strip().str.replace(',', '').astype(float)

# Limpeza na força bruta - Começo

df2 = df.copy()
df2 = df2.drop(df2.index)
country = df['Country'].unique()
min_year = df['Year'].min()
max_year = df['Year'].max()
all_years = pd.DataFrame({'Year': range(min_year, max_year + 1)})
years = all_years['Year']

# for c in country:
#     for y in years:
#         new_row = {'Country': c, 'Region': get_region(df,c), 'Year': y, 'GDP_pp': get_gdp_pp(df, c, y)}
#         df2 = pd.concat([df2, pd.DataFrame([new_row])], ignore_index=True)
# export_csv(df2,path_file,'df2') #Virou o arquivo df3.csv

# Limpeza na força bruta - Fim


print('Antes')
print(df3.head(16))
inter = df3.groupby('Country')['GDP_pp'].apply(lambda group: group.interpolate(method='linear'))


# teste_inter = pd.DataFrame({'GDP_pp': inter})
teste_inter = inter.to_frame()
teste_inter2 = teste_inter.reset_index()
df3['GDP_pp'] = teste_inter2['GDP_pp']

# print(df3)

print('\nDepois')
print(df3.head(16))