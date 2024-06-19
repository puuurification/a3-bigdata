import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import apoio as ap

df_gdp = pd.read_csv('data/GDP_interpolated.csv')
df_obesity = pd.read_csv('data/obesity-cleaned.csv')

df_gdp.drop(columns=['Year'], inplace=True)
df_obesity.drop(columns=['Obesity_percentual'], inplace=True)

ap.correcao_paises_obesidade(df_obesity)
df_gdp = ap.remocao_paises_ausentes(df_gdp)
df_obesity = ap.remocao_paises_ausentes(df_obesity)

merge = pd.merge(df_gdp,df_obesity, on=['Country','year'])
max_year = merge.year.max()
south_america = merge[(merge['Region']=='South America') & (merge['year'] == max_year) & (merge['Sex'] == 'Both sexes')]
# increase_south = south_america.sort_values(by=['obesity_cumsum_diff'], ascending=False)
increase_south = south_america.sort_values(by=['Obesity'], ascending=False)
# print(south_america.sort_values(by=['obesity_cumsum_diff'], ascending=False))


N = 7
X = increase_south['Country'].head(N) 
# Ygirls = increase_south['obesity_cumsum_diff'].head(N) 
Ygirls = increase_south['Obesity'].head(N) 


X_axis = np.arange(len(X)) 

plt.bar(X_axis, Ygirls, 0.2) 

plt.xticks(X_axis, X) 
# plt.xlabel("Regiões") 
# plt.ylabel("Acumulo de PIB") 
plt.title("Rank de Obesidade") 
# plt.savefig('img/figure6.png')
plt.show()