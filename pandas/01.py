"""
You are given a pandas DataFrame df that may contain missing values (nulls). Write a function solution(df) that cleans the data by following these rules, in order:

Drop any column whose fraction of missing values is greater than 0.5.
After dropping those columns, drop any row whose fraction of missing values (across the remaining columns) is greater than 0.5.
Fill the remaining missing values: for numeric columns use the column mean, and for non-numeric (object/string) columns use the column's most frequent value (the first mode if there are ties).
Return the resulting DataFrame with its index reset (0, 1, 2, ...).

Example:
Input:
df = pd.DataFrame({'a':[1,2,None,4],'b':[None,3,4,5],'c':['x',None,'x','y']})
Output:
   a    b  c
0  1.0  4.0  x
1  2.0  3.0  x
2  2.333333  4.0  x
3  4.0  5.0  y
"""

# Solution:
import pandas as pd
import numpy as np

def solution(df):

    # 1. Columns:
    col_missing_frac= df.isna().mean()
    df= df.drop(columns= col_missing_frac[col_missing_frac > 0.5].index)

    # 2. Rows:
    row_missing_frac= df.isna().mean(axis= 1)
    df= df.drop(index= row_missing_frac[row_missing_frac > 0.5].index)

    # 3. Filling Missing Values:
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            mode = df[col].mode(dropna=True)
            if not mode.empty:
                df[col] = df[col].fillna(mode.iloc[0])

    # 4. Resetting Index:
    return df.reset_index(drop= True)    