import numpy as np
import pandas as pd

def rough_number(a, arr1):
    lower_appr = upper_appr = 0.0

    count1 = count2 = 0
    sum1 = sum2 = 0.0
    for j in range(0, len(arr1)):
        if arr1[j]<=a:
            count1 += 1
            sum1 = sum1 + arr1[j]
        if arr1[j]>=a:
            count2 += 1
            sum2 += arr1[j]
            
    lower_appr = sum1/count1
    upper_appr = sum2/count2
    return [lower_appr, upper_appr];

writer = pd.ExcelWriter('/home/saif/Documents/Project/rev_rough_no.xlsx', engine='xlsxwriter')
for iteration in range(1,13):
    dataset = pd.read_excel('/home/saif/Documents/Project/rev_data.xlsx', sheet_name ='FM'+str(iteration))
    rn = list()
    data = np.zeros(shape=(6,42))
    for i in range(0,21):
        arr1 = dataset.iloc[:, i+1].values
        for j in range(0, 5):
            u = arr1[j]
            rn = rough_number(u, arr1)
            data[j][2*i] = rn[0]    
            data[j][2*i+1] = rn[1]
        if i%7 == 0 or i%7 == 4:
            data[5][2*i] = min(data[:5,2*i])
            data[5][2*i+1] = min(data[:5, 2*i+1])
        elif i%7 == 3 or i%7 == 6:
            data[5][2*i] = max(data[:,2*i])
            data[5][2*i+1] = max(data[:, 2*i+1])
        else:
            data[5][2*i] = sum(data[:,2*i])/5
            data[5][2*i+1] = sum(data[:, 2*i+1])/5
    j=0
    interval = np.zeros(21)
    for i in range(1,42,2):
        interval[j] = data[5][i] - data[5][i-1]
        j += 1
    df1 = pd.DataFrame(data, index=['D1', 'D2', 'D3', 'D4', 'D5', 'avg'])
    df2 = pd.DataFrame({'FM'+str(iteration): interval})
    df1.to_excel(writer, sheet_name='FM'+str(iteration), header=False,)
    df2.to_excel(writer, sheet_name='interval_diff', startcol=iteration-1, index=False)
writer.save()


