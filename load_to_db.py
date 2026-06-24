import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Data/db/bluestock_mf.db")

print("Database created successfully!")

nav_df = pd.read_csv("Data/Processed/clean_nav_history.csv")
transactions_df = pd.read_csv("Data/Processed/clean_investor_transactions.csv")
performance_df = pd.read_csv("Data/Processed/clean_scheme_performance.csv")

nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)

transactions_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)

performance_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("All tables loaded successfully!")