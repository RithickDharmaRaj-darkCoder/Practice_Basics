# Set Datatype ...

a = {"Rithick","Dharma","Raj"}
c = {"1,2,3,4,5"}
print("Normal Set :",a,"\n--------------------")
b = a.copy()
print("copy () :",b,"\n--------------------")

d = a.union(c)
print("union () :",d,"\n--------------------")

a.update(c)
print("update () :",a,"\n--------------------")