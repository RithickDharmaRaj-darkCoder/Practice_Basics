# Numerical Patterns ...

a = "Rithick dharma RAJ"
print(a,'\n'+"lower() :",a.lower(),"\n--------------------")

a = "*     Rithick     *"
print(a,'\n'+"lstrip() :",a.lstrip("* "))
print("rstrip() :",a.rstrip("* "))
print("strip() :",a.strip("* "),"\n--------------------")

a = "RITHICK dHARMA RAJ"
b = a.maketrans("d","D")
print(a,'\n'+"maketrans() & translate() :",a.translate(b),"\n--------------------")

a = "Rithick Dharma Raj"
print(a,'\n'+"partition() :",a.partition("Dharma"),"\n--------------------")

a = "Raj Raj Cholan"
print(a,'\n'+"replace() :",a.replace("Raj","Raja",1))
print(a,'\n'+"replace() :",a.replace("Raj","Raja",2))
print(a,'\n'+"replace() :",a.replace("Raj","Raja"),"\n--------------------")

a = "Rithick Raj, Dharma Raj"
print(a,'\n'+"rfind() :",a.rfind("Raj"),"\n--------------------")

print(a,'\n'+"rindex() :",a.rindex("Raj"),"\n--------------------")
