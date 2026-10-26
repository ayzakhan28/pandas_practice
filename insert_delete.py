import pandas as pd
data={"name": ["Ali", "Ahmad","hina","Aqsa"],
      "Age":[12,23,32,21],
      "marks":[35,55,70,80]
      }
df=pd.DataFrame(data)
df["city"]=["faisalabad", "Sangla", "lahore","Propian"]
df.insert(4, "class",[11,12,14,15])
df=df.assign(cast=["jutt","butt","Ansari","Arain"])
print(df)

df["Age"]=df["Age"]+1
print(df)
df.loc[2, "Age"]=18
print(df)

df.drop("Age",axis=1,inplace=True) #smjna ha ye 
df.drop(2, axis=0, inplace=True)
print(df)

