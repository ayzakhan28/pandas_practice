import pandas as pd

data = {
    "name": ["Ali", "Hina", "Ahmad", "Aqsa"],
    "marks": [80, 45, 65, 90]
}

df = pd.DataFrame(data)

df["result"]=df["marks"].map( lambda marks:  "Pass" if marks>=60  else "Fail")
df["name_uppercase"]=df["name"].map(str.upper)

print(df)




df = pd.DataFrame({
    "name": ["Ali", "Hina", "Ahmad", "Aqsa"],
    "class": ["A", "B", "A", "C"],
    "marks":[56,76,44,32],
    "age":[23,21,24,25]
})

df["class"] = df["class"].map({
    "A": "Excellent",
    "B":"Good",
    "C":"Fair"

})

print(df)

def check_result(marks):
    if marks>=50:
        return" Pass" 
    else:
        return "Fail"

df["result"]=df["marks"].apply(check_result)
print(df)
    

df["total"]=df.apply(
    lambda row: row[ "marks"]+ row["age"], axis=1
)    
print(df)
