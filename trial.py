# String Methods...

a = "Rithick Dharma Raj"
print(a,'\n'+"isspace() :",a.isspace())
a = "    "
print(a,'\n'+"isspace() :",a.isspace(),'\n--------------------')

a = 'Rithick dharma Raj'
print(a,'\n'+"istitle() :",a.istitle())
a = "Rithick Dharma Raj"
print(a,'\n'+"istitle() :",a.istitle(),'\n--------------------')

a = "Rithick dharma RAJ"
print(a,'\n'+"isupper() :",a.isupper())
a = "17 RITHICK DHARMA RAJ *+-"
print(a,'\n'+"istitle() :",a.isupper(),'\n--------------------')

a = ("Rithick","Dharma","Raj")
print(a,'\n'+"join() :","-".join(a),'\n--------------------')

a = {'Fname':"Rithick",'Lname':"Dharma Raj"}
print(a,'\n'+"formate_map() :","{Fname} is also called as "
"{Lname}".format_map(a),'\n--------------------')

a = "Rithick"
print(a,"\n"+"ljust() :",a.ljust(10,'^'),".darkCoder",'\n--------------------')

a = "Rithick"
print(a,"\n"+"rjust() :",a.rjust(10,'*'),".darkCoder",'\n--------------------')
