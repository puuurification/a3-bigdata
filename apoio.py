import pandas as pd

def correcao_paises_obesidade(df_obesity):
    countries_gdp = ['Bolivia','Brunei','Cape Verde','Congo, Rep.','Iran','Korea, Dem. Rep.','Korea, Rep.','Macedonia, FYR','Micronesia, Fed. Sts.','Russia','Slovak Republic','Sudan','Syria','Tanzania','United Kingdom','United States','Venezuela','Vietnam','Yemen, Rep.','Czech Rep.',"Cote d'Ivoire",'Laos','Moldova']
    contries_obesity = ['Bolivia (Plurinational State of)','Brunei Darussalam','Cabo Verde','Congo','Iran (Islamic Republic of)',"Democratic People's Republic of Korea",'Republic of Korea','Republic of North Macedonia','Micronesia (Federated States of)','Russian Federation','Slovakia','Sudan (former)','Syrian Arab Republic','United Republic of Tanzania','United Kingdom of Great Britain and Northern Ireland','United States of America','Venezuela (Bolivarian Republic of)','Viet Nam','Yemen','Czechia',"Côte d'Ivoire","Lao People's Democratic Republic",'Republic of Moldova']

    for index in range(0,len(contries_obesity)):
        df_obesity['Country'] =  df_obesity['Country'].replace(contries_obesity[index],countries_gdp[index])
    
    return df_obesity

def remocao_paises_ausentes(df):
    countries = ['Greenland','Kosovo','Liechtenstein','Monaco','San Marino','South Sudan','Swaziland','Taiwan','Central African Republic','Cook Islands','Democratic Republic of the Congo','Dominican Republic','Eswatini','Niue']
    # for country in countries:
    df = df[~df['Country'].isin(countries)]
    return df