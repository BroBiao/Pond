import pandas as pd
import random


file_path = './data/test_addresses.parquet'
df = pd.read_parquet(file_path, engine='pyarrow')
print(df.head().to_string())

pred_df = pd.DataFrame()
pred_df['ADDRESS'] = df['ADDRESS']
for i in range(len(pred_df)):
    pred_df.loc[i, 'PRED'] = round(random.random())
pred_df['PRED'] = pred_df['PRED'].astype('int')
print(pred_df)

pred_df.to_csv('./pred.csv', index=False)
pred = pd.read_csv('./pred.csv')
print(pred)