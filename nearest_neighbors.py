import numpy as np
import pandas as pd

Q = [130775.0, 5947.0324, 0.203, 0.0083, 144.0, 81.0, 1.0435]
Neighbors = 20
reffile = 'processed_front.pf'
datafile = 'processed_front.pf'
selected_columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO'] #['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']

def fsi_numpy(arr, item_id):
    tmp_arr = arr - arr[item_id]
    tmp_ser = np.sum( np.square( tmp_arr ), axis=1 )
    return tmp_ser

Q = np.genfromtxt('nearest_neighbors.in')    
df = pd.read_csv(datafile, delimiter=' ')
df.loc[len(df)] = Q
df = df.drop_duplicates()
#df = df.reset_index(drop=True)
ref = pd.read_csv(reffile, delimiter=' ')
df_norm = (df - ref.min()) / (ref.max() - ref.min())
mat = df_norm.as_matrix(columns=selected_columns)
df2=df.copy();
df2['dist'] = fsi_numpy(mat , len(df2)-1)
df2 = df2.sort_values(by='dist').head(Neighbors)
#print df2



