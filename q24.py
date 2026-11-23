import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "titanic.csv")

df = pd.read_csv(csv_path)

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

if "Cabin" in df.columns:
    df.drop(columns=["Cabin"], inplace=True)

df.drop_duplicates(inplace=True)
df["Sex"] = df["Sex"].str.lower().str.strip()
df["Age"] = df["Age"].astype(int)

print(df.info())
print(df.head())