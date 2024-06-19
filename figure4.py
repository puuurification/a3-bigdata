import numpy as np  
import matplotlib.pyplot as plt
import analise_merge as merge


countries = ['United States','Brazil','Portugal']
max_year = merge.merge.year.max()
data_obes = merge.merge[(merge.merge['Country'].isin(countries)) & (merge.merge['year'] == max_year) & (merge.merge['Sex'] == 'Both sexes')].sort_values(by=['Obesity'], ascending=False)
data_obes['GDP_pp'] = data_obes['GDP_pp']/1000

N = 3
ind = np.arange(N)  
width = 0.25

xvals = data_obes['GDP_pp'].head(N)
bar1 = plt.bar(ind, xvals, width, color = 'g') 

yvals = data_obes['Obesity'].head(N)
bar2 = plt.bar(ind+width, yvals, width, color='r') 

plt.xlabel("Países") 
# plt.ylabel('GDP_pp/100 X Obesity') 
plt.title("GDP_pp/1000 X Obesity")

plt.xticks(ind+width,data_obes['Country'].head(N)) 
plt.legend( (bar1, bar2), ('GDP_pp', 'Obesity') ) 
plt.savefig('img/figure4.png')
plt.show()