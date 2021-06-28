import pandas as pd
import json
import os 

dir_str = './data/preprocessed/0/'

df = pd.read_csv(dir_str + 'vnexpress_v2.csv', index_col = 0)

print(df.shape[0] / 3)
print(df.shape[0] / 3 * 2)

df_1 = df.iloc[:10183]
df_2 = df.iloc[10183:20367]
df_3 = df.iloc[20367:]

for i, dfs in enumerate([df_1, df_2, df_3]):
    dfs.to_csv(dir_str + f'vnexpress_{i}.csv')
