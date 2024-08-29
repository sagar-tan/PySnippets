import pandas as pd
import numpy as np
def handle_miss(df):
    missing_values = df.isnull().sum()#the sum count all the values and is null returns the poitns
    print(f"Missing values in each column:{missing values}")
    numeric_cols = df.select_dtypes(include = [np.number]).columns#selects columns with numbers
    for col in numeric_cols:
        median_value = df[col].median()
        df[col].fillna(median_value, inplace=True)
    categorical_cols = df.select_dtypes(include = [object]).columns #selects columns with objects
    for col in categorical_cols:
        mode_val= df[col].mode()[0]
        df[col].fillna(mode_val, inplace=True)
    df.dropna(how='all', inplace=True)
    return df
data={
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, np.nan, 'cat', 'dog'],
    'C': [np.nan, 2.5, 3.0, np.nan]
}
df = pd.DataFrame(data)
print('Original Dataframe:')
print(df)
 df= handle_miss(df)
 print(df)
