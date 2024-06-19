import pandas as pd
import apoio as ap

df_gdp = pd.read_csv('data/GDP_interpolated.csv')
df_obesity = pd.read_csv('data/obesity-cleaned.csv')

df_gdp.drop(columns=['Year','Region'], inplace=True)
df_obesity.drop(columns=['Obesity_percentual'], inplace=True)

ap.correcao_paises_obesidade(df_obesity)
df_gdp = ap.remocao_paises_ausentes(df_gdp)
df_obesity = ap.remocao_paises_ausentes(df_obesity)


merge = pd.merge(df_gdp,df_obesity, on=['Country','year'])
merge = merge[['Country','year','GDP_pp','GDP_pp_diff','GDP_pp_cumsum_diff','Sex','Obesity','obesity_diff','obesity_cumsum_diff']]

# merge.to_csv("data/merge.csv", index=False)
# print(merge)

max_year = merge.year.max()
# view = merge[merge['Sex'] == 'Both sexes'].sort_values(by=['GDP_pp_cumsum_diff'],ascending=False).to_csv('data/view.csv')
# view = merge[(merge['year'] == max_year) & (merge['Sex'] == 'Both sexes')].sort_values(by=['GDP_pp_cumsum_diff'], ascending=False).head(5).to_csv('data/view.csv',index=False)
view = merge[(merge['year'] == max_year) & (merge['Sex'] == 'Both sexes')].sort_values(by=['Obesity'], ascending=False).head(5).to_csv('data/view.csv',index=False)
# view = merge[merge['Sex'] == 'Both sexes'].sort_values(by=['year'], ascending=False).to_csv('data/view.csv',index=False)
# print(merge.sort_values(by=['GDP_pp_cumsum_diff']))