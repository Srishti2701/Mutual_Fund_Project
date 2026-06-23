import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_data = data["data"]

    df = pd.DataFrame(nav_data)

    print(name)
    print(df.head())

    df.to_csv(f"Data/Raw/{name}_nav.csv", index=False)

    print(f"{name} data saved successfully!\n")