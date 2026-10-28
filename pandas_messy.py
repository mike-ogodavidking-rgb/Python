import pandas as pd

df = pd.read_csv("messy.csv")

df["name"] = df["name"].str.strip().str.title()
df["course"] = df["course"].str.strip().str.title()
df = df.drop_duplicates()

print(df)

print(df.groupby("course")["score"].mean())

cleaned = df.dropna()
print(cleaned)

cleaned.to_csv("cleaned_messy.csv", index=False)
