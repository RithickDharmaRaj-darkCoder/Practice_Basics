# Dictionary Datatype ...

a = {'Fname':'Rithick','hobby':'coding'}
print(f'Normal Dictionary : {a}'
      f'\n--------------------')

b = a.get('Fname')
print(f'get () : {b}')
b = a.get('Lname','Dharma Raj')
print(f'get () : {b}\n--------------------')

d = a.keys()
a['relax'] = 'Games'
print(f'Normal Dictionary () : {a}\n'
      f'keys () : {d}\n--------------------')

a = ('Dept1','Dept2','Dept3')
b = ('CSE')
c = dict.fromkeys(a,b)
print(f'fromkeys () : {c}\n--------------------')

d = c.items()
print(f'items () : {d}\n--------------------')

d = c.copy()
print(f'copy () : {d}\n--------------------')