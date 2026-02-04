"""
Day 12 Activity: String & Date Cleaning
Tasks:
1) Clean city strings (strip, lower, remove punctuation)
2) Map synonyms to canonical values
3) Parse mixed-format timestamps and localize to UTC
"""

import pandas as pd

df = pd.read_csv('Day 12 + CSV/day12_users.csv')

df['city'] = df["city"].str.strip().str.lower()


df["city_cleaned"] = (
 df["city"]
 .str.replace("-", " ", regex=False)  
 .str.replace(r"[^a-z\s]", "", regex=True)  
 .str.replace(r"\s+", " ", regex=True).str.strip())  

canonical_map = {"new york": "new york", "nyc": "new york", "ny": "new york",
 "san francisco": "san francisco", "sanfrancisco": "san francisco"}

df["city_token"] = df["city_cleaned"].str.replace(" ", "", regex=False)
df["city_canonical"] = df["city_token"].map(canonical_map).fillna(df["city_cleaned"])

df["signup_dt_raw"] = pd.to_datetime(df["signup_time"], errors="coerce", infer_datetime_format=True)

print(df)
print("NaT count:", df["signup_dt_raw"].isna().sum())
# TODO: Implement standardize_city(df)
# TODO: Implement parse_and_localize(df)
# TODO: Print cleaned columns for inspection
