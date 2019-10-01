"""
pack2 - a limited set of df engineering tools
"""

import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split

# code to train/test/val split a df

def splitter(df):
    train,test = train_test_split(df, train_size=.8)
    train,val = train_test_split(train, train_size=.8)
    print(train,test,val)

def detail_na(df):
    nas = df.isna().sum()
    print(nas)



