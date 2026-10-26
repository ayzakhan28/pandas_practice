import pandas as pd
data={
    "Name": ["Ali", "Ahmad", "Hassan", "Farqan"],
    "Age": [24,56,34,32],
    "Marks": [89,67,90,89]
}

df=pd.DataFrame(data)

print(df.head())

y=[2,4,6,8,99]


x=pd.Series(y, index=['a','d','b','h','f'],dtype="float",name="python")
print(x)

s=pd.Series(12)
print(s)

y=pd.Series(12,index=[1,2,3,4,5,6])
z=pd.Series(13, index=[1,2,3,4])
print(y+z)