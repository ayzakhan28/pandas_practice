import pandas as pd 
var =pd.DataFrame({"s":[5,7,8,9,3], "r":[2,3,4,4,6]}
)
print(var)

var["addition"]=var["s"]+var["r"]


var["Subtract"]= var["s"]-var["r"]

var["Divide"]=var["s"] / var["r"]

var["multipy"]=var["s"] * var["r"]


print(var)


var["python"]= var["s"] <5
print(var)