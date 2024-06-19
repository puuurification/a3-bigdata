
import numpy as np  
import matplotlib.pyplot as plt
import relatorio as rel
import analise_merge as merge

def regioes_maior_crescimento():
    rel.regions

    X = rel.regions['Region'].head(3) 
    Ygirls = rel.regions['GDP_pp_cumsum_diff'].head(3) 
    
    X_axis = np.arange(len(X)) 
    
    plt.bar(X_axis, Ygirls, 0.2) 
    
    plt.xticks(X_axis, X) 
    plt.xlabel("Regiões") 
    plt.ylabel("Acumulo de PIB") 
    plt.title("Maiores crescimentos de PIB") 
    plt.savefig('img/figure1.png')


# def paises_obesos():
max_year = merge.merge.year.max()
data_obes = merge.merge[(merge.merge['year'] == max_year) & (merge.merge['Sex'] == 'Both sexes')].sort_values(by=['Obesity'], ascending=False)
data_obes['GDP_pp_cumsum_diff'] = data_obes['GDP_pp_cumsum_diff']/100

print(data_obes['GDP_pp_cumsum_diff'].head(2))

N = 5
ind = np.arange(N)  
width = 0.25

xvals = data_obes['GDP_pp_cumsum_diff'].head(N)
bar1 = plt.bar(ind, xvals, width, color = 'g') 

yvals = data_obes['Obesity'].head(N)
bar2 = plt.bar(ind+width, yvals, width, color='r') 

# zvals = [rel.df_union_describe_sexes['Homens'].loc['Máximo'], rel.df_union_describe_sexes['Mulheres'].loc['Máximo']] 
# bar3 = plt.bar(ind+width*2, zvals, width, color = 'b') 

plt.xlabel("Países") 
# plt.ylabel('Values') 
# plt.title("Males X Females") 

plt.xticks(ind+width,data_obes['Country'].head(N)) 
plt.legend( (bar1, bar2), ('GDP_pp_cumsum_diff', 'Obesity') ) 
plt.savefig('img/figure2.png')
# plt.show()


max_year = merge.merge.year.max()
data_gdp = merge.merge[(merge.merge['year'] == max_year) & (merge.merge['Sex'] == 'Both sexes')].sort_values(by=['GDP_pp_cumsum_diff'], ascending=False)
data_gdp['GDP_pp_cumsum_diff'] = data_gdp['GDP_pp_cumsum_diff']/1000



N = 5
ind = np.arange(N)  
width = 0.25

print(data_gdp.head(N))

print(data_gdp['GDP_pp_cumsum_diff'].head(N))

xvals = data_gdp['GDP_pp_cumsum_diff'].head(N)
bar1 = plt.bar(ind, xvals, width, color = 'g') 

yvals = data_gdp['Obesity'].head(N)
bar2 = plt.bar(ind+width, yvals, width, color='r') 

# zvals = [rel.df_union_describe_sexes['Homens'].loc['Máximo'], rel.df_union_describe_sexes['Mulheres'].loc['Máximo']] 
# bar3 = plt.bar(ind+width*2, zvals, width, color = 'b') 

plt.xlabel("Países") 
# plt.ylabel('Values') 
# plt.title("Males X Females") 

plt.xticks(ind+width,data_gdp['Country'].head(N)) 
plt.legend( (bar1, bar2), ('GDP_pp_cumsum_diff', 'Obesity') ) 
plt.savefig('img/figure3.png')
# plt.show()



regioes_maior_crescimento()
# paises_obesos()