import pandas as pd

products = pd.read_csv('products.csv')
customers = pd.read_csv('customers1.csv')
orders = pd.read_csv('orders.csv')


df = pd.merge(orders, customers, on="Customer ID")
df = pd.merge(df, products, on="ProductID")

df["TotalAmount"] = df["Quantity"]*df["Price"]
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["OrderMonth"] = df["OrderDate"].dt.month

df = df[df["Quantity"] >= 2]
df = [df["Country"].isin(["India","UAE"])]

category_summary = df.groupby("Category", as_index=False)["TotalAmount"].sum()
segment_summary = df.groupby("Segment", as_index=False)["TotalAmount"].sum()

df=df.sort_values(by= "TotalAmount",ascending=False)

df.to_csv("product_orders.csv", index = False)
category_summary.to_csv("category_summary.csv", index = False)
segment_summary.to_csv("segment_summary.csv", index = False)




