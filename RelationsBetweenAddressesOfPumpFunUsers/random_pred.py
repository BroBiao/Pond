import pandas as pd
import random


file_path = './data/test_set.parquet'
df = pd.read_parquet(file_path, engine='pyarrow')
print(df)

res_df = pd.DataFrame()
res_df['PAIR_ID'] = df['PAIR_ID']
for i in range(len(res_df)):
    res_df.loc[i, 'PRED'] = round(random.random(), 1)
print(res_df)

res_df.to_csv('./res.csv', index=False)
res = pd.read_csv('./res.csv')
print(res)