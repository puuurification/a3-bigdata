
import numpy as np  
import matplotlib.pyplot as plt
import relatorio as rel
import analise_merge as merge


max_year = merge.merge.year.max()
data_gdp = merge.merge[(merge.merge['year'] == max_year) & (merge.merge['Sex'] == 'Both sexes')].sort_values(by=['GDP_pp'], ascending=False)
data_gdp['GDP_pp'] = data_gdp['GDP_pp']/1000

N = 5
ind = np.arange(N)  
width = 0.25

xvals = data_gdp['GDP_pp'].head(N)
bar1 = plt.bar(ind, xvals, width, color = 'g') 

yvals = data_gdp['Obesity'].head(N)
bar2 = plt.bar(ind+width, yvals, width, color='r') 


plt.xlabel("Países") 
# plt.ylabel('GDP_pp/1000 X Obesity')
plt.title("GDP_pp/1000 X Obesity") 

plt.xticks(ind+width,data_gdp['Country'].head(N)) 
plt.legend( (bar1, bar2), ('GDP_pp', 'Obesity') ) 
plt.savefig('img/figure3.png')
# plt.show()