import pandas as pd
import sys
import os

file_dir = os.path.dirname(__file__)

def merge_csv():
    df1 = pd.read_csv(os.path.join(file_dir,"../dataset/csv1.csv"))
    df2 = pd.read_csv(os.path.join(file_dir,"../dataset/csv2.csv"))
    
    result_df = pd.merge(df1, df2, on='name')
    
    result_df.to_csv(os.path.join(file_dir,"../dataset/csv3.csv"))

if __name__ == "__main__":
    merge_csv()