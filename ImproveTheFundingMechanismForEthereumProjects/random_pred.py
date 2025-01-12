import pandas as pd
import random


file_path = './data/test.csv'
df = pd.read_csv(file_path, engine='pyarrow')
# print(df)

pred_df = pd.DataFrame()
pred_df['id'] = df['id']
for i in range(len(pred_df)):
    pred_df.loc[i, 'pred'] = random.random()
print(pred_df)

pred_df.to_csv('./pred.csv', index=False)
pred = pd.read_csv('./pred.csv')
print(pred)