"""
Day 13 Activity: Large Dataset Cleaning
Tasks:
1) Read CSV in chunks
2) Clean each chunk (e.g., numeric conversion)
3) Append cleaned chunks to output CSV
4) Track basic performance metrics
"""

import pandas as pd
import time

chunks = pd.read_csv("Day 13 + CSV/day13_large_users.csv")

for chunk in chunks:
    chunks["age"] = pd.to_numeric(chunks["age"], errors="coerce")
    chunks["income"] = pd.to_numeric(chunks["income"], errors="coerce")

print(chunks)


"""  """





# TODO: Implement clean_chunk(df)
# TODO: Implement process_large_file(path_in, path_out, chunksize)
