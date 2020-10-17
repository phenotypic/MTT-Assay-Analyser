import string
import statistics
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Mean cell viability (%) = ((mean absorption - blank absorption) / (control absorption - blank absorption)) * 100

parser = argparse.ArgumentParser()
parser.add_argument('type')
parser.add_argument('-o', action='store_true')
args = parser.parse_args()

df = pd.read_csv(args.type + '.csv', header=None)

drugCount = int(df.shape[1] / 4)
drug = {}
deviation = {}

for x in range(drugCount):
    startCol = x * 4
    drug[x] = {}
    deviation[x] = {}

    controlAbsorb = df.iloc[0:7][startCol].mean()
    # blank = df.iloc[7][startCol:startCol+4].mean()  # For mean blank
    for subCol in range(4):
        blank = df.iloc[7][startCol + subCol]  # For column blank
        drug[x][subCol] = ((df.iloc[0:7][startCol + subCol].mean() - blank) / (controlAbsorb - blank)) * 100
        deviation[x][subCol] = statistics.stdev(df.iloc[0:7][startCol + subCol])

columns = list(string.ascii_uppercase[0:drugCount])
labels = ['Control', 'High', 'Medium', 'Low']

df = pd.DataFrame(drug)
deviation = pd.DataFrame(deviation)

df.columns = columns
df.index = labels
deviation.columns = columns
deviation.index = labels

if args.o:
    df.to_csv(args.type + '-raw-data.csv')
    deviation.to_csv(args.type + '-stdev-data.csv')

df.T.plot(kind='bar', yerr=list(deviation.values*100), color=['C0', 'C3', 'C1', 'C2'])

list = PrettyTable(['Concentration', 'Best', 'Worst'])

for row in range(1, 4):
    best = df.iloc[row].idxmin() + ' (' + str(round(df.iloc[row].min())) + ' %)'
    worst = df.iloc[row].idxmax() + ' (' + str(round(df.iloc[row].max())) + ' %)'
    list.add_row([labels[row], best, worst])

print('\nDrug analysis for', args.type, 'cells:')
print(list, '\n')

plt.xlabel('Drug')
plt.ylabel('Mean cell viability (%)')
plt.legend(labels=labels, title='Concentration')
plt.title('Viability of ' + args.type + ' cells against drugs A-' + string.ascii_uppercase[drugCount - 1])

plt.show()
