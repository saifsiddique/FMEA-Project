import pandas as pd
from numpy import zeros
from math import gamma

def beta_func(x, alpha, beta):
    
    if alpha == 0:
        return 0
    a = (gamma(alpha+beta)/(gamma(alpha)*gamma(beta)))*(x**(alpha-1))*((1-x)**(beta - 1))
    return a

alphas = pd.read_excel('/home/saif/Documents/Project/mean_sd1.xlsx', sheet_name ='alpha')
betas = pd.read_excel('/home/saif/Documents/Project/mean_sd1.xlsx', sheet_name ='beta')

x = 0.25 #float(input('Enter time '))
final = zeros(shape = (3,12))
for i in range(3):
    for j in range(12):
        final[i][j] = beta_func(x, -1*alphas.iloc[i][j], betas.iloc[i][j])
writer = pd.ExcelWriter('/home/saif/Documents/Project/final_rank2.xlsx', engine='xlsxwriter')
df = pd.DataFrame(final)
df.to_excel(writer, sheet_name = '0.25', index = False, header = False)
writer.save()