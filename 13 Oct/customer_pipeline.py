import pandas as pd

df = pd.read_csv("customers.csv")

df.dropna(inplace=True)

df["Age"] = df["Age"].astype(int)
df = df[df["Age"] >= 20]

df["AgeGroup"] = df["Age"].apply(lambda x:"Young" if x < 30 else ("Adult" if x < 50 else "Senior"))

df.to_csv("filtered_customers.csv", index = False)

print("Data pipeline completed.Filtered data saved to filtered_customers.csv")

