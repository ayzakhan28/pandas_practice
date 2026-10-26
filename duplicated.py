import pandas as pd

data = {
    "name": ["Ali", "Hina", "Ali", "Aqsa", "Hina"],
    "marks": [80, 90, 80, 70, 90],
    "age": [20, 22, 20, 24, 22]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nDuplicate rows:")
print(df.duplicated())

print("\nTotal duplicate rows:")
print(df.duplicated().sum())

df = df.drop_duplicates(subset="name")

print("\nDataFrame after removing duplicates:")
print(df)
