import pandas as pd
import os
folder = "Data/raw"

files = os.listdir(folder)
print(files)

for file in files:
    path= os.path.join(folder,file)
    
    df= pd.read_csv(path)
    print(file)

    print(df.shape)
    print(df.dtypes)
    print(df.head())
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nDuplicate rows:")
    print(df.duplicated().sum())