import pandas as pd
import random


address_file_path = './data/test_addresses.parquet'
addr_df = pd.read_parquet(address_file_path, engine='pyarrow')
print(addr_df.tail().to_string())

protocol_file_path = './data/allowed_protocols.parquet'
pro_df = pd.read_parquet(protocol_file_path, engine='pyarrow')
print(pro_df.head().to_string())

pred_df = pd.DataFrame()
for i in range(len(addr_df)):
    protocols_index = random.choices(list(range(len(pro_df))), k=5)
    for j in range(5):
        pred_df.loc[i*5+j, 'WALLET'] = addr_df.loc[i, 'ADDRESS']
        pred_df.loc[i*5+j, 'REC'] = pro_df.loc[protocols_index[j], 'PROTOCOL']
print(pred_df)

pred_df.to_csv('./pred.csv', index=False)
pred = pd.read_csv('./pred.csv')
print(pred)