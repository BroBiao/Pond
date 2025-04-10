import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


train_file_path = './data/GGAllocationSinceGG18.csv'
train_df = pd.read_csv(train_file_path)
train_df['ConPerCap'] = train_df['Contribution Amount'] / train_df['# of Contributors']
train_df_sorted = train_df.sort_values(by='ConPerCap')
filter_width = 50
X = train_df_sorted[['# of Contributors']][filter_width:-filter_width].values
y = train_df_sorted['Contribution Amount'][filter_width:-filter_width].values

model = LinearRegression()
model.fit(X, y)
slope = model.coef_[0]
intercept = model.intercept_
# print(slope, intercept)

test_file_path = './data/mydata.csv'
test_df = pd.read_csv(test_file_path)
pred_file_path = './data/projects_Mar_31.csv'
pred_df = pd.read_csv(pred_file_path)
pred_df['AMOUNT'] = test_df['NUM'] * slope + intercept
pred_df.to_csv('./pred.csv', index=False)
pred = pd.read_csv('./pred.csv')