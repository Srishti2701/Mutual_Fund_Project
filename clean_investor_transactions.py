import pandas as pd
df = pd.read_csv("Data/Raw/08_investor_transactions.csv")

print(df.head())
print(df.dtypes)
print(df["transaction_type"].unique())
print(df[df["amount_inr"]<=0])
print(df["kyc_status"].unique())
df["transaction_date"]= pd.to_datetime(df["transaction_date"])
print(df.dtypes)
print("Duplicate rows:",df.duplicated().sum())

df.to_csv("Data/Processed/clean_investor_transactions.csv", index=False)
print("Cleaned investor transactions saved successfully!")