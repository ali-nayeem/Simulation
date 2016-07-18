import pandas as pd
from pandas.tools.plotting import parallel_coordinates
import matplotlib.pyplot as plt
reffile = 'processed_front.pf'
datafile = 'processed_front.pf'
columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']
new_columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']
unit = 0.1285
title = 'Mandl-4 Reference Front'

df = pd.read_csv(datafile, delimiter=' ')
df = df.drop_duplicates()
df = df.reset_index(drop=True)

ref = pd.read_csv(reffile, delimiter=' ')
df_norm = (df - ref.min()) / (ref.max() - ref.min())

for i in range(0, len(columns)):
    new_columns[i] = columns[i] + ' (' + str(round(ref[columns[i]].min(),2)) + ')'
    #df_norm = df_norm.drop( df_norm[df_norm[columns[i]] > 1].index )
    #df_norm = df_norm.drop( df_norm[df_norm[columns[i]] < 0].index )
df_norm.columns = new_columns
df_norm['ID'] = df_norm.index
parallel_coordinates(df_norm,'ID', colormap='prism').legend_.remove()
for i in range(1, len(columns)+1):
    plt.figtext(i*unit,0.92,'(' + str(round(ref[columns[i-1]].max(),2)) + ')',ha='center')
plt.suptitle(title)
plt.show()
