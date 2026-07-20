"""
You are given a DataFrame df with two columns: group (a categorical key) and value (a numeric column). 
Add a new column named group_avg that contains, for each row, the average of value computed over all rows sharing the same group. 
Return the resulting DataFrame with the original columns plus the new group_avg column, preserving the original row order.

Example:
Input:
df = pd.DataFrame({'group': ['a','a','b'], 'value': [10, 20, 40]})
Output:
  group  value  group_avg
0     a     10       15.0
1     a     20       15.0
2     b     40       40.0
"""

# Solution:
import pandas as pd

def solution(df):
    temp= df.copy()
    temp['group_avg']= temp.groupby('group')['value'].transform('mean')
    return temp