import pandas as pd

data = {
    "name": ["Ali", "Hina", "Ahmad", "Aqsa"],
    "marks": [80, None, 65, None],
    "Age": [20, 22, None, 24]
}

df = pd.DataFrame(data)


print(df)
print(df.isna())
print(df.isna().sum())
print(df.notna().sum())
# print(df.dropna(subset=["marks"]))
# df["marks"]=df["marks"].fillna(0)

df["marks"]=df["marks"].fillna(50)
# df["marks"]=df["marks"].fillna(df["marks"].mean())
# df["marks"]=df["marks"].fillna(df["marks"].median())
# df["marks"]=df["marks"].ffill()
# df["marks"]=df["marks"].bfill()
print(df)

data = {
    "name": ["Ali", "Hina", "Ahmad", "Aqsa"],
    "marks": [80, None, 65, None],
    "age": [20, 22, None, 24]
}
df = pd.DataFrame(data)


df["age"]=df["age"].fillna(df["age"].mean())
df["marks"]=df["marks"].fillna(df["marks"].median())


print(df)

print(df["age"].mean())