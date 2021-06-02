# String Methods...

a = 'RITHICK DHARMA RAJ'
print("Normal String :",a,'\n-------------------')

a = 'RITHICK\tDHARMA\tRAJ'
b = a.expandtabs(6)
print("expandtabs() :",b,'\n--------------------')

b = a.find("K")
print("find() :",b)
b = a.find("u")
print("find() :",b,'\n-------------------') #not found = -1.

a = 'Rithick {name} Raj'
b = a.format(name = 'Dharma')
print("formate() :",b,'\n-------------------')

a = 'RithickDharmaRaj17'
print("isalnum() :",a.isalnum())
a = "@#!$%"  #Space also gives False.
print("isalnum() :",a.isalnum(),'\n-------------------')

a = 'RithickDharmaRaj17'
print("isalpha() :",a.isalpha())
a = "@#!$%"  #Space also gives False.
print("isalpha() :",a.isalpha(),'\n-------------------')

b = a.index('!')
print("index() :",b,'\n')
b = a.index('u')
print("index() :",b,'\n-------------------') #not found = error!.
