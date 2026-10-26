import pandas as pd
data={
    "Name": ["Ali", "Ahmad", "Hassan", "Farqan"],
    "Age": [24,56,34,32],
    "Marks": [89,67,90,89]
}

df=pd.DataFrame(data)
print(df)
print(data["Name"][3])

list_1={"s":pd.Series([3,4,5,6,7,8,9]), "r":pd.Series([9,8,7,76,5,3,2])}
h=pd.DataFrame(list_1)
print(h)


data={"name": ["Ali", "Ahmad","HIna","Aysha"],
      "Age": [23,32,22,12],
      }

df=pd.DataFrame(data)

print(df)
print(df.shape)
print(df.columns)
print(df.loc[1])
df.index=[12,20,30,40]
print(df)
print(df.loc[20, "name"])
print(df.iloc[1, 0])
