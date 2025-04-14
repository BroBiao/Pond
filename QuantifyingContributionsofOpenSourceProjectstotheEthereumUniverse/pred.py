import pandas as pd


file_path = './data/test.csv'
df = pd.read_csv(file_path)
# print(df)

proj_count = len(df['repo'])
author_list = []
for i in range(proj_count):
    author_list.append(df.loc[i, 'repo'].split('/')[-2])

parent_list = df['parent'].to_list()

for i in range(proj_count):
    author = df.loc[i, 'repo'].split('/')[-2]
    author_weight = author_list.count(author) / proj_count
    parent = df.loc[i, 'parent']
    parent_weight = parent_list.count(parent) / proj_count
    total_weight = author_weight + parent_weight
    df.loc[i, 'weight'] = total_weight

df.to_csv('./pred.csv', index=False)
res = pd.read_csv('./pred.csv')
print(res)