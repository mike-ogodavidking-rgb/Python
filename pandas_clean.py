import pandas as pd

df = pd.read_csv("scores.csv")

print(df.isna().sum())

cleaned = df.dropna()
print(cleaned)

print(cleaned.groupby("course")["score"].mean())

cleaned.to_csv("cleaned_scores.csv", index=False)