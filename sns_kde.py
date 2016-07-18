import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set(style="white")

datafile = 'processed_front.pf'
df = pd.read_csv(datafile, delimiter=' ')
#df = df.round(decimals=6)
df = df.drop_duplicates()
df = df.reset_index(drop=True)
df = (df - df.min()) / (df.max() - df.min())

g = sns.PairGrid(df, diag_sharey=False)
g.map_lower(sns.kdeplot, cmap="Blues_d")
g.map_upper(plt.scatter)
g.map_diag(sns.kdeplot, lw=3)

plt.show()