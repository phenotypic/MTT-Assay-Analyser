import string
import statistics
import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# %viability = ((absorbtion - blank absorbtion) / (control absorbtion - blank absorbtion)) * 100

cell = 'HeLa'

df = pd.read_csv(cell + '.csv', header=None)

drugCount = int(df.shape[1] / 4)

drug = {}
deviation = {}

for x in range(drugCount):
    startCol = x * 4
    drug[x] = {}
    deviation[x] = {}

    blank = df.iloc[7][startCol:startCol+4].mean()  # If you want to use mean blank for each drug
    for subCol in range(4):
        drug[x][subCol] = ((df.iloc[0:7][startCol+subCol].mean() - df.iloc[7][startCol+subCol]) / (df.iloc[0:7][startCol].mean() - df.iloc[7][startCol+subCol])) * 100
        deviation[x][subCol] = statistics.stdev(df.iloc[0:7][startCol+subCol])

df = pd.DataFrame(drug)
deviation = pd.DataFrame(deviation)
df.columns = list(string.ascii_uppercase[0:drugCount])
df.T.plot(kind='bar', yerr=list(deviation.values*100), color=['C0', 'C3', 'C1', 'C2'])

labels = ['Control', 'High', 'Medium', 'Low']
list = PrettyTable(['Concentration', 'Best', 'Worst'])

for row in range(1, 4):
    best = df.iloc[row].idxmin() + ' (' + str(round(df.iloc[row].min())) + ' %)'
    worst = df.iloc[row].idxmax() + ' (' + str(round(df.iloc[row].max())) + ' %)'
    list.add_row([labels[row], best, worst])

print('\nDrug analysis for', cell, 'cells:')
print(list, '\n')

plt.xlabel('Drug')
plt.ylabel('Mean cell viability (%)')
plt.legend(labels=labels, title='Concentration')
plt.title('Viability of ' + cell + ' cells against drugs A-' + string.ascii_uppercase[drugCount - 1])

plt.show()
