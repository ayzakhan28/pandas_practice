import pandas as pd
data={"name": ["Ali", "Ahmad","hina","Aqsa"],
      "Age":[12,23,32,21],
      "marks":[35,55,70,80]
      }

df=pd.DataFrame(data)

print(df[df["marks"]>60])
print(df)
print(
df[(df["marks"]>70)    &( df["Age"]>20)])
print(df[(df["marks"]>70) | (df["Age"]>20)])
print(df[df["name"].isin(["Ali", "hina"])])
print(df[df["marks"].between(40,80)])

print(df[(df["name"].isin(["Ali","hina"]))])
print(df[df["marks"].between(25,80)])
print(df[(df["marks"]>80 | (df["Age"]> 35))])
print(df[df["name"].str.contains("a", case=False)])
print(df[df["name"].str.startswith("A")])
print(df[df["name"].str.endswith("a")])

print(df.loc[df["marks"]>60, ["name", "marks"]])

print(df[df["marks"].isna()])
print(df[df["name"].notna()])