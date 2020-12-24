import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_excel('F:/Files/Study/TinyLarry/Projects/Data Wrangling Python/data/raw data.xlsx', engine='openpyxl')
print(df.head())

### create 'earlier_date' column: ###
### choose the earlier date of 'grad_date' and 'wedding_date' ###

df['earlier_date'] = df[['grad_date', 'wedding_date']].min(axis=1)
print(df)

### create 'first_notnull_date' column: ###
### choose first not null date of 'grad_date' and 'wedding_date' ###
df['first_notnull_date'] = df['wedding_date']
df.loc[df['grad_date'] != np.datetime64('NaT'), 'first_notnull_date']  = df['grad_date']
print(df)

### create 'country_income_gap' column: ###
### calculate the difference of income and max income of the country ###
df['country_income_gap'] = df.groupby(['country'])['income'].transform('max') - df['income']
print(df)