import pandas as pd
datafile = 'TNDP-FUN-DF.txt'
df = pd.read_csv(datafile, delimiter=' ')
df_norm = (df - df.min()) / (df.max() - df.min())
df_norm.to_csv('Normalized-'+datafile, sep=' ', header=False, index = False)
