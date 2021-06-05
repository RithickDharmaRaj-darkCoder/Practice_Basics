# List Datatype ...

lst1 = ["Rithick","Dharma","Raj"]
lst2 = lst1.copy()
print('Normal List :',lst1,'\n'+"copy :",lst2,'\n--------------------')

lst3 = ['raja','raja','cholan']
print("count () :",lst3.count('raja'),'\n--------------------')

print("index () :",lst1.index("Dharma"),'\n--------------------')

lst1.reverse()
print("reverse () :",lst1,'\n--------------------')

lst1.sort()
print("sort (Ascending) :",lst1)
lst1.sort(reverse=True)
print("sort (Descending) :",lst1,'\n--------------------')