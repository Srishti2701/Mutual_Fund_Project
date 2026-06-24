import pandas as pd 
df = pd.read_csv("Data/Raw/02_nav_history.csv")
print(df.head())
print(df.dtypes)
df["date"]=pd.to_datetime(df["date"])
print(df.dtypes)

df= df.sort_values(by=["amfi_code","date"])
print(df.head())

print(df.isnull().sum())
print("Duplicate rows:",df.duplicated().sum())
print(df[df["nav"]<=0])
df.to_csv("Data/Processed/clean_nav_history.csv",index=False)
print("Cleaned NAV History saved successfully")