# Set Datatype ...

a = {"Rithick","Dharma","Raj"}
b = {"Rithick",".darkCoder"}
print("Normal Set :",a)
print("Normal Set :",b,'\n--------------------')

c = a.difference(b)
d = b.difference(a)
print("difference () :",c)
print("difference () :",d,'\n--------------------')

a.difference_update(b)
b.difference_update(a)
print("difference_update () :",a)
print("difference-update () :",b,'\n--------------------')

a.discard("Raj")
print("discord () :",a,'\n--------------------')

s = {1,2,3,4,5,6}
t = {4,5,6,7,8}
e = t.intersection(s)
print("intersection () :",e,'\n--------------------')

t.intersection_update(s)
print("intersection_update () :",t,'\n--------------------')
