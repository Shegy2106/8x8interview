import pandas as pd
import sys
import os

file_dir = os.path.abspath(os.path.dirname(__file__))

def merge_csv():
    csv1_path = os.path.join(file_dir,"../dataset/csv1.csv")
    if not os.path.exists(csv1_path):
        print(f"File {csv1_path} does not exist")

    csv2_path = os.path.join(file_dir,"../dataset/csv2.csv")
    if not os.path.exists(csv2_path):
        print(f"File {csv2_path} does not exist")

    df1 = pd.read_csv(csv1_path)
    df2 = pd.read_csv(csv2_path)
    
    result_df = pd.merge(df1, df2, on='name')
    
    csv3_path = os.path.join(file_dir,"../dataset/csv3.csv")

    try:
        result_df.to_csv(csv3_path)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    merge_csv()