import pandas as pd
from datetime import datetime
import numpy as np

def export_csv(dataframe, path_file,dataframe_file_name):
    dataframe.to_csv(path_file+dataframe_file_name+'.csv', index=False)
    print('DataFrame Exportado')

# path_file = 'GDP/'
file_path = 'GDP/GDP.xls'

gdp_brute = pd.read_csv("GDP/GDP.xls")
# gdp_brute = pd.read_excel(file_path,engine='calamine')
df = gdp_brute.copy()
df['temp_year'] = pd.to_datetime(gdp_brute['Year']) 
df['Year'] = df['temp_year'].dt.year
df.drop(columns=['temp_year'], inplace=True)
df.rename(columns={'GDP_pp': 'Per_capita'}, inplace=True) #Não consigo realizar funções com essa coluna 'GDP_pp'
# df['Per_capita'] = df['Per_capita'].astype(float)

print(df)