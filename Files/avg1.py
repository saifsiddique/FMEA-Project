import pandas as pd
import numpy as np
from math import sqrt

def avg(arr):
    return sqrt((sum(arr[:4])/4)*(sum(arr[4:])/3)) #((sum(arr[:4])/4) + sqrt((sum(arr[:4])/4)*(sum(arr[4:])/3)))
def sd(arr):
    return sqrt((np.std(arr[:4], ddof=1))*(np.std(arr[4:], ddof=1))) #((np.std(arr[:4], ddof=1)) + sqrt((np.std(arr[:4], ddof=1))*(np.std(arr[4:], ddof=1))))
def alp(mu, sigma):
    if sigma == 0:
        return 0
    alpha = -(mu*(sigma*sigma+mu*mu-mu))/(sigma*sigma)
    return alpha
def bet(mu, sigma):
    if sigma == 0:
        return 0
    beta = ((mu-1)*(sigma*sigma+mu*mu-mu))/(sigma*sigma)
    return beta
    
dataset = pd.read_excel('/home/saif/Documents/Project/rev_rough_no.xlsx', sheet_name ='interval_diff')
writer = pd.ExcelWriter('/home/saif/Documents/Project/mean_sd1.xlsx', engine='xlsxwriter')
mu = np.zeros(shape=(3,12))
sigma = np.zeros(shape=(3,12))
alpha = np.zeros(shape=(3,12))
beta = np.zeros(shape=(3,12))

for i in range(12):
    temp = dataset.iloc[:, i]
    k=0
    for j in range(0,21,7):
        mu[k][i] = avg(temp[j:j+7])
        sigma[k][i] = sd(temp[j:j+7])
        alpha[k][i] = alp(mu[k][i], sigma[k][i])
        beta[k][i] = bet(mu[k][i], sigma[k][i])
        k=k+1
df1 = pd.DataFrame(mu)
df2 = pd.DataFrame(sigma)
df3 = pd.DataFrame(alpha)
df4 = pd.DataFrame(beta)
df1.to_excel(writer, sheet_name='Mean', header= False, index=False)
df2.to_excel(writer, sheet_name='StdDev', header= False, index=False)
df3.to_excel(writer, sheet_name='alpha', header= False, index=False)
df4.to_excel(writer, sheet_name='beta', header= False, index=False)
writer.save()
