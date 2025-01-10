import pandas as pd
import random


file_path = './data/test_tokens/test_tokens.parquet'
df = pd.read_parquet(file_path, engine='pyarrow')
print(df.head().to_string())

pred_df = pd.DataFrame()
pred_df['ADDRESS'] = df['TOKEN_ADDRESS']
for i in range(len(pred_df)):
    pred_df.loc[i, 'PRED'] = round(random.uniform(-1, 1)*10, 1)
print(pred_df)

pred_df.to_csv('./pred.csv', index=False)
pred = pd.read_csv('./pred.csv')
print(pred)