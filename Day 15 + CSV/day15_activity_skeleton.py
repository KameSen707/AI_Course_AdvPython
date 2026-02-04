"""
Day 15 Activity: Mini Project — End-to-End Cleaning
Tasks:
1) Load raw dataset
2) Design a cleaning plan (types, missing, outliers, strings, dates)
3) Implement clean_data_project
4) Save cleaned dataset
5) Document decisions
"""

import pandas as pd
import csv

df = pd.read_csv("Day 15 + CSV/day15_real_dataset.csv")

def clean_types(df):
    out = df.copy()
    out["age"] = pd.to_numeric(out["age"], errors="coerce")
    out["income"] = pd.to_numeric(out["income"], errors="coerce")
    return out

def clean_missing(df):
    out = df.copy()
    out["age"] = out["age"].fillna(out["age"].median())
    return out

def handle_outliers(df):
    upper_99 = df["income"].quantile(0.99)
    mask_keep = df["income"] <= upper_99
    df_removed = df[mask_keep].copy()
    return df_removed

def clean_strings_and_dates(df):
    out = df.copy()
    mapping = {
        "ny" : "new york",
        "sf" : "south fransisco",
        "la" : "los angeles",
    }

    out["city"] = out["city"].str.strip().str.lower()
    out["city"] = (out["city"].str.replace("-", " ", regex=False).str.replace(r"[^a-z\s]", "", regex=True).str.replace(r"\s+", " ", regex=True).str.strip()) 
    out["city"] = out["city"].map(mapping)
    out["signup_time"] = pd.to_datetime(out["signup_time"], errors="coerce")
    return out


def validate_cleaned(df):
    assert df["age"].min() >= 0, "Negative ages found"
    assert df["income"].notna().all(), "Income still has NaN"

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = clean_types(df)
    df = clean_missing(df)
    df = handle_outliers(df)
    df = clean_strings_and_dates(df)
    validate_cleaned(df)  
    return df

df = clean_data(df)

# TODO: Save cleaned dataset to data/day15_cleaned.csv

df.to_csv('day15_cleaned.csv', index=False)