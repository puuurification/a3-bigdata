
import numpy as np  
import matplotlib.pyplot as plt
import relatorio as rel

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
plt.show()