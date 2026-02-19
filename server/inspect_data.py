import pandas as pd

df = pd.read_csv("data/recruitment_data.csv")

print("\nHEAD:")
print(df.head())

print("\nCOLUMNS:")
print(df.columns)

print("\nTARGET DISTRIBUTION:")
# ⚠️ On ne connaît pas encore le nom exact de la target
print(df.iloc[:, -1].value_counts())
