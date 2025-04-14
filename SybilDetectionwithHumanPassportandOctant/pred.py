import pandas as pd
import numpy as np
from scipy.stats import norm


# base_train_file = './data/base_sybil_detection/train_addresses.parquet'
# base_train_df = pd.read_parquet(base_train_file, engine='pyarrow')
# print(len(base_train_df[base_train_df['LABEL'] == 1]))
# print(len(base_train_df[base_train_df['LABEL'] == 0]))

# base_test_file = './data/base_sybil_detection/test_addresses.parquet'
# base_test_df = pd.read_parquet(base_test_file, engine='pyarrow')

eth_tx_file = './data/ethereum_sybil_detection/transactions.parquet'
eth_tx_df = pd.read_parquet(eth_tx_file, engine='pyarrow')
eth_from_addr = eth_tx_df['FROM_ADDRESS'].to_list()
eth_to_addr = eth_tx_df['TO_ADDRESS'].to_list()
eth_tx_addr = eth_from_addr + eth_to_addr

eth_train_file = './data/ethereum_sybil_detection/train_addresses.parquet'
eth_train_df = pd.read_parquet(eth_train_file, engine='pyarrow')
eth_sybils = eth_train_df[eth_train_df['LABEL'] == 1]['ADDRESS'].to_list()
eth_sybils_tx = []
for addr in eth_sybils:
    eth_sybils_tx.append(eth_tx_addr.count(addr))
mu, std = norm.fit(eth_sybils_tx)

eth_test_file = './data/ethereum_sybil_detection/test_addresses.parquet'
eth_test_df = pd.read_parquet(eth_test_file, engine='pyarrow')
for i in range(len(eth_test_df)):
    test_addr_tx = eth_tx_addr.count(eth_test_df.loc[i, 'ADDRESS'])
    eth_test_df.loc[i, 'PRED'] = round(np.exp(-((test_addr_tx - mu)**2) / (2 * std**2)), 2)

eth_test_df.to_csv('./pred.csv', index=False)
pred = pd.read_csv('./pred.csv')
print(pred)