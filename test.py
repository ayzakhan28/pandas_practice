import pandas as pd

df=pd.read_csv("students.csv")
print(df.shape)
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isna().sum())

print(df.groupby("class")["student_id"].count())
print(df.groupby("class"))
print(df[df["class"]=="A"])

print()


print("Marks greater than 80 ")
print()
print(df[df["marks"]>=80])

print()
print("Marks greater than 80 of Students class A ")
print()
print(df.groupby("class"))
print(df[(df["class"]=="A") & (df["marks"]>=80)])

print(df[(df["city"]=="Lahore") | (df["city"]=="Faisalabad")])


print(df[df["marks"].between(60,80)])



print("Sorted data")
print(df["marks"].sort_values(ascending=False))

print(df["marks"].sort_values(ascending=False).head(5))

print(df["marks"].agg(["mean","median","max","min"]))
print(df.groupby("class")["marks"].mean())
print(df.groupby("class")["student_id"].count())



print("Missing Values of data ")

print(df.isna().sum())

print(df[df["marks"].isna()])
df["marks"]=df["marks"].fillna(df["marks"].mean())
df["attendance"]=df["attendance"].fillna(df["attendance"].mean())
print(df)



print(df[df.duplicated()])
print(df.duplicated().sum())
print(df["name"].duplicated().sum())

df=df.drop_duplicates(subset="name")
print(df)


print("New Column or analysis")

df["result"]=df["marks"].map( lambda marks: "Pass" if marks>50 else "Fail")
print(df)

def check_result(marks):
    if pd.isna("marks"):
        return "Misssing.."
    if marks >=80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >=50:
        return "C"
    else:
        return "Fail"

df["Grade"]=df["marks"].apply(check_result)
print(df)    



print(df.groupby("city")["student_id"].count())

print(df.groupby("class")["attendance"].corr(df["marks"]))



print("Top Five students list")

top_five=df.sort_values(by ="marks", ascending=False).head(5)
print(top_five)
print(df.groupby("class")["marks"].mean())
top_two=df.sort_values(by ="marks" ,ascending=False).groupby("class").head(2)
print(top_two)
