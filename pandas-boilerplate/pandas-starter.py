import pandas as pd

data = pd.read_csv("sample-data.csv")

print("First 5 Rows:")
print(data.head())

print("\nSummary Statistics:")
print(data.describe())

print("\nColumn Names:")
print(data.columns)