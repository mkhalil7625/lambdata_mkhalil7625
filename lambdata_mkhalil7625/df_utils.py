import pandas as pd
import numpy as np
ONES = pd.Series(np.ones(10))
ZEROS = pd.Series(np.zeors(20))
def NULL_Check (df):
    if df.isnull().vlues.any():
        num_null = df.isnull().sum().sum()
        print('The dataframe contains '+num_null+' NAN values')
    else:
        print('The dataframe does not contain NAN values')

def List_Column(list)
    ser = pd.Series(list)
    return df['new_col']=ser.values

List_to_df_column = List_Column(l)
Check_Nulls=NULL_Check(df)
