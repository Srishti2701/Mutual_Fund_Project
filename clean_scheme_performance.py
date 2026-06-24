import pandas as pd
df = pd.read_csv("Data/Raw/07_scheme_performance.csv")
print(df.head())
print(df.dtypes)
negative_sharpe = df[df["sharpe_ratio"]<=0]
print(negative_sharpe)
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]
print(invalid_expense)
print(df.isnull().sum())
df.to_csv(
    "Data/Processed/clean_scheme_performance.csv",
    index=False
)
print("Cleaned scheme performance saved successfully!")