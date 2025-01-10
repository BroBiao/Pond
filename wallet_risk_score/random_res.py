import pandas as pd
import random


file_path = './test_addresses.parquet'
df = pd.read_parquet(file_path, engine='pyarrow')

for i in range(len(df)):
    df.loc[i, 'PRED'] = int(round(random.random()))
df['PRED'] = df['PRED'].astype('int')

df.to_csv('./test_addresses.csv', index=False)
res = pd.read_csv('./test_addresses.csv')


# -----------------------------------------------

# file_path = './train_addresses.parquet'
# df = pd.read_parquet(file_path, engine='pyarrow')
# print(len(df))
# print(df.tail())