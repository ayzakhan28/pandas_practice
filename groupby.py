import pandas as pd

data = {
    "name": ["Ali", "Ahmad", "Hina", "Aqsa", "Sara", "Usman"],
    "class": ["A", "B", "A", "B", "A", "B"],
    "marks": [80, 60, 90, 70, 85, 75]
}

df = pd.DataFrame(data)

print(df)

print(df.groupby("class")["marks"].mean())
print(df.groupby("class")["marks"].sum())
print(df.groupby("class")["name"].count())
print(df.groupby("class")["marks"].max())
print(df.groupby("class")["marks"].min())
print(df.groupby("class")["marks"].agg(["count", "mean","max","min"]))

df["age"]=[20,24,18,23,22,25]
print(df)

print(df.groupby("class")[["marks","age"]].agg(["count","mean","max","min"]))

print(df.groupby("class").agg({
    "marks":["mean","max","min"],
    "age":["mean","max","min"]
}))


print(df["class"].value_counts())

print(df["marks"].value_counts(normalize=True)*100)

print(df.sort_values("marks"))

print(df.sort_values("age",ascending=False))


