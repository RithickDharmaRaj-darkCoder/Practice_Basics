# Numerical Patterns ...

a = "Rithick Raj Rithick Dharma Raj"
print(a,"\n"+"rpartition () :",a.rpartition("Rithick"),'\n--------------------')

a = "Rithick, Dharma, Raj, 17"
print(a,"\n"+"rsplit () :",a.rsplit(", ",1))
print("rsplit () :",a.rsplit(", ",2))
print("rsplit () :",a.rsplit(", "),'\n--------------------')

print(a,"\n"+"split () :",a.split(", ",1))
print("split () :",a.split(", ",2))
print("split () :",a.split(", "),'\n--------------------')

a = "Rithick \nDharma \nRaj"
print(a,'\n'+"splitlines () :",a.splitlines())
print("splitlines () :",a.splitlines(False))
print("splitlines () :",a.splitlines(True),'\n--------------------')

a = "Rithick dharma raj"
print(a,'\n'+"startswith () :",a.startswith("Rithick"))
print(a,'\n'+"startswith () :",a.startswith("d",8),'\n--------------------')

print(a,'\n'+"swapcase () :",a.swapcase(),'\n--------------------')

print(a,'\n'+"title () :",a.title(),'\n--------------------')