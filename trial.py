# String Methods...

a = '2\u00B2' #unicode of (2 power 2)
print(a,'\n'+"isdecimal() :",a.isdecimal())
a = '\u0031'  #unicode of 1
print(a,'\n'+"isdecimal() :",a.isdecimal(),'\n--------------------')

a = "2\u00B2"  #unicode of (2 power 2)
print(a,'\n'+"isdigit() :",a.isdigit())
a = "1"
print(a,'\n'+"isdigit() :",a.isdigit(),'\n--------------------')

a = "17Rithickdark Coder"
print(a,'\n'+"isidentifier() :",a.isidentifier())
a = "Rithick17dark_Coder"
print(a,'\n'+"isidentifier() :",a.isidentifier(),'\n--------------------')

a = 'Rithick DHARMA raJ'
print(a,'\n'+"islower() :",a.islower())
a = '* rithick dharma raj 17'
print(a,'\n'+"islower() :",a.islower(),'\n--------------------')

a = "-17.17"
print(a,'\n'+"isnumeric() :",a.isnumeric())
a = "17\u00B2"
print(a,'\n'+"isnumeric() :",a.isnumeric(),'\n--------------------')

a = "Rithick\tDharma Raj"   #\t can't able to print...
print(a,'\n'+"isprintable() :",a.isprintable())
a = "RithickDharma Raj #17"
print(a,'\n'+"isprintable() :",a.isprintable())