import pandas as pd
import matplotlib.pyplot as plt
datafile = 'processed_front.pf'
columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']
new_columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']
start = 0.184
unit = 0.11
df = pd.read_csv(datafile, delimiter=' ')
#df = df.round(decimals=6)
df = df.drop_duplicates()
df_norm = (df - df.min()) / (df.max() - df.min())
for i in range(0, len(columns)):
    new_columns[i] = columns[i] + ' (' + str(round(df[columns[i]].min(),2)) + ')'
    df_norm = df_norm.drop( df_norm[df_norm[columns[i]] > 1].index )
    df_norm = df_norm.drop( df_norm[df_norm[columns[i]] < 0].index )
df_norm.columns = new_columns
df_norm.boxplot()
for i in range(0, len(columns)):
    plt.figtext(start+i*unit,0.91,'(' + str(round(df[columns[i]].max(),2)) + ')',ha='center')
plt.suptitle('Mandl-4')
plt.show()
