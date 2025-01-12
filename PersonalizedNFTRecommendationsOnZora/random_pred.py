import pandas as pd
import random


wallet_file_path = './data/test_addresses.parquet'
wallet_df = pd.read_parquet(wallet_file_path, engine='pyarrow')
print(wallet_df.tail().to_string())

contract_file_path = './data/contracts.parquet'
nft_df = pd.read_parquet(contract_file_path, engine='pyarrow')
print(nft_df.tail().to_string())

pred_df = pd.DataFrame()
for i in range(len(wallet_df)):
    print(str(i+1) + '/' + str(len(wallet_df)))
    nft_index = random.choices(list(range(len(nft_df))), k=5)
    for j in range(5):
        pred_df.loc[i*5+j, 'WALLET'] = wallet_df.loc[i, 'ADDRESS']
        pred_df.loc[i*5+j, 'REC'] = nft_df.loc[nft_index[j], 'ADDRESS']
print(pred_df)

pred_df.to_csv('./pred.csv', index=False)
pred = pd.read_csv('./pred.csv')
print(pred)