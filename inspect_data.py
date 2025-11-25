import pandas as pd

df = pd.read_csv(r"E:\ml-churn-api\data\churn-bigml-80.csv")

print(df.head())
print(df.columns)
print(df["Churn"].value_counts())  # replace with actual churn column name
