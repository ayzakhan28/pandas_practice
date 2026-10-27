import pandas as pd

students = pd.DataFrame({
    "student_id": [101, 102, 103],
    "name": ["Ali", "Sara", "Hamza"]
})

marks = pd.DataFrame({
    "student_id": [101, 102, 103],
    "marks": [85, 92, 76]
})

combine=pd.merge(students,marks, on="student_id", how="inner")
print(combine)

combine=pd.merge(students,marks, on="student_id", how="left")
print(combine)


combine=pd.merge(students,marks, on="student_id", how="right")
print(combine)


combine=pd.merge(students,marks, on="student_id", how="outer")
print(combine)


#Concatenation 

df1 = pd.DataFrame({
    "name": ["Ali", "Sara","Hafsa"],
    "marks": [85, 90,97]
})

df2 = pd.DataFrame({
    "name": ["Hamza", "Ayesha", "Iqra"],
    "marks": [78, 95, 90]
})

# Dono DataFrames ko rows ke through combine karna
result = pd.concat([df1,df2],axis=0, ignore_index=True)  #axis=0 — rows ko ek ke neeche ek add karta hai. Ye default hai.
result=pd.concat([df1,df2], axis=1)    #- axis=1 — columns ko side-by-side add karta hai.

print(result)