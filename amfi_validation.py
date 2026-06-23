import pandas as pd

# Read datasets
fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")

# Create sets of unique AMFI codes
master_codes = set(fund_master["amfi_code"])

nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = master_codes - nav_codes

print("Missing codes:")

print(missing_codes)