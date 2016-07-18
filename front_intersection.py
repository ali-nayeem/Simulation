import pandas as pd
from pandas.tools.plotting import parallel_coordinates
import matplotlib.pyplot as plt

df1Path = 'E:/Msc@BUET/Thesis/multiobjective transit network/Simulation/Front/Mandl-4/RF/Mandl-4.pf'
df2Path = 'E:/Msc@BUET/Thesis/multiobjective transit network/Simulation/Front/Mandl-4/SPEA2/Mandl-4.rf'
columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']
unit = 0.1285
title = 'SPEA2'

def pc(df, ref):
    new_columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']
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

df1 = pd.read_csv(df1Path, delimiter=' ')
df1 = df1.drop_duplicates()
df1 = df1.reset_index(drop=True)

df2 = pd.read_csv(df2Path, delimiter=' ')
df2 = df2.drop_duplicates()
df2 = df2.reset_index(drop=True)

s1 = pd.merge(df1, df2, how='inner', on=columns)
s1.dropna(inplace=True)
#pc(s1, df1)
s1_norm = (s1 - df1.min()) / (df1.max() - df1.min())