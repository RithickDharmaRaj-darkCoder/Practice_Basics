# Dictionary Datatype ...

a = {'Fname':'Rithick','hobby':'coding'}
print(f'Normal Dictionary : {a}'
      f'\n--------------------')
b = a.values()
print(f'values () : {b}\n--------------------')

a.update({'Lname':'Dharma Raj'})
print(f'update () : {a}\n--------------------')

b = a.setdefault('Fname','RDR')
print(f'setdefault () : {b}\n--------------------')

a.pop('hobby')
print(f'pop () : {a}\n--------------------')

a.popitem()
print(f'popitems () : {a}\n--------------------')

a.clear()
print(f'clear () : {a}\n--------------------')