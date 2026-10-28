import pandas as pd

df = pd.read_csv("scores.csv")

print(df)
print(df.head(3))
print(df.shape)
print(df.columns)
print(df.describe())
print(df[df["course"] == "Maths"])
print(df["score"].mean())
print(df[df["score"] < 50])