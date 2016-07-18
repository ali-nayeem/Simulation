import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
datafile = 'processed_front.pf'
df = pd.read_csv(datafile, delimiter=' ')
#df = df.round(decimals=6)
df = df.drop_duplicates()
df_norm = (df - df.min()) / (df.max() - df.min())
#df_norm.to_csv('TNDP-FUN-DF-norm.txt', sep=' ', header=False, index = False)
axes = scatter_matrix(df_norm, alpha=0.2, figsize=(30, 30), diagonal='kde')
corr = df_norm.corr().as_matrix()
for i, j in zip(*plt.np.triu_indices_from(axes, k=1)):
    axes[i, j].annotate("%.3f" %corr[i,j], (0.8, 0.8), xycoords='axes fraction', ha='center', va='center')
plt.subplots_adjust(wspace=0.07, hspace=0.15) 
plt.suptitle('Mandl-4')
plt.show()
#parallel_coordinates(df_norm,'ID',colormap='prism').legend_.remove() df_norm['ID'] = df_norm.index
