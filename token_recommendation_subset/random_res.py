import pandas as pd
import random


file_path = './training_tokens.parquet'
df = pd.read_parquet(file_path, engine='pyarrow')

new_df = pd.DataFrame()
new_df['ADDRESS'] = df['TOKEN_ADDRESS']
rank_list = [i+1 for i in list(range(len(new_df)))]

addr_list = new_df['ADDRESS'].to_list()
sorted_addr = sorted(addr_list, key = lambda addr: addr[::-1])
print(sorted_addr)

for i in range(len(new_df)):
    address = new_df.loc[i, 'ADDRESS']
    rank = random.choice(rank_list)
    new_df.loc[i, 'RANK'] = rank
    rank_list.remove(rank)
new_df['RANK'] = new_df['RANK'].astype('int')
print(new_df)

# new_df.to_csv('./token_rank.csv', index=False)
# res = pd.read_csv('./token_rank.csv')
# print(res)