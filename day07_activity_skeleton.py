"""
Day 7 Activity: Imputation Practice
Tasks:
1) Implement fit_imputer(train_df) returning medians/modes
2) Implement transform_imputer(df, params)
3) Add missing indicators optionally
4) Compare behavior with/without indicators
"""

import pandas as pd

# Sample dataset
train = pd.DataFrame({
    "age": [25, None, 40, 33],
    "city": ["NY", "SF", None, "NY"],
})

test = pd.DataFrame({
    "age": [None, 50],
    "city": ["SF", None],
})

def fit_imputer(train_df, num_cols, cat_cols):
    medians = (train_df[num_cols].median())
    modes = (train_df[cat_cols].mode())
    return medians, modes 
medians, modes = fit_imputer(train, "age", "city")

train ["age"] = train ["age"].fillna(medians)
train ['city']= train ['city'].fillna(modes[0])
    

def transform_imputer(df, params, add_indicators=True):
    num, cat = params

    df[num] = df[num].fillna(medians)
    df[cat] = df[cat].fillna(modes)

print(train)


"""
    Fit imputer on training data to get medians for numerical columns
    and modes for categorical columns.

    Parameters:
    train_df (pd.DataFrame): Training dataframe
    num_cols (list): List of numerical column names
    cat_cols (list): List of categorical column names

    Returns:
    dict: Dictionary with 'num_medians' and 'cat_modes'
    """

# TODO: Implement fit_imputer
# def fit_imputer(train_df, num_cols, cat_cols):
#     ...

# TODO: Implement transform_imputer
# def transform_imputer(df, params, add_indicators=True):
#     ...
