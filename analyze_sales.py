import pandas as pd

df = pd.read_csv("sales.csv")

print("Total Sales:", df["Sales"].sum())
print(df.groupby("Product")["Sales"].sum())
