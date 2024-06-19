print(merge)


# print(df_obesity[df_obesity['Country'] == 'Bolivia'])
# print(teste[teste['Country'] == 'Bolivia'])

country_gdp = df_gdp['Country'].unique()
print(len(country_gdp))
country_obesity = df_obesity['Country'].unique()
print(len(country_obesity))

# df_union_country = pd.DataFrame({
#     'country_gdp': country_gdp,
#     'country_obesity': country_obesity
# })

# print(df_union_country)

df_union_country = pd.DataFrame({
    'country_gdp':country_gdp,
})


df_union_country_2 = pd.DataFrame({
    'country_obesity': country_obesity
})

view = df_union_country.loc[~df_union_country['country_gdp'].isin(country_obesity)] #.to_csv("data/drop.csv", index=False)
view2 = df_union_country_2.loc[~df_union_country_2['country_obesity'].isin(country_gdp)] #.to_csv("data/drop.csv", index=False)
print('Paise do GDP que nao tem no Obesidadade')
print(view)

print('Paise do Obesidadade que nao tem no GDP')
print(view2)
# print(country_gdp)
# print(len(country_gdp))
# df_union_country['country_obesity'] = country_obesity
# print(df_union_country)
# print(df_union_country.loc[~df_union_country['country_gdp'].isin(country_obesity)])
# print(df_union_country[df_union_country['country_gdp'].str.contains('Bolivia') == True])
# print(df_union_country.loc[df_union_country['country_gdp'] == 'Bolivia'])
# df_union_country.loc[~df_union_country['country_gdp'].isin(country_obesity)].reset_index(drop=True).to_csv("data/countrys.csv", index=False)