import pandas as pd

df = pd.read_excel('F:/Files/Study/TinyLarry/Projects/Data Wrangling Python/data/raw data.xlsx', engine='openpyxl')
print(df.head())

# create 'earlier_date' column: choose the earlier date of 'college_grad_date' and 'wedding_date'
df['earlier_date'] = df[['grad_date', 'wedding_date']].min(axis=1)
print(df)