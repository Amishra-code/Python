# dictionary

data={1:'Anjali', 2:'Prerna', 3:'Anchal'}
print(data)

print(data[1])
# print(data[4])                     # error

print(data.get(1))
print(data.get(4))                   # no error: prints 'None'

print(data.get(2,'Not found'))       # no error : prints 'Prerna'
print(data.get(4,'Not found'))       # no error : prints 'Not found'


keys=['Anjali', 'Prerna', 'Anchal']  # list 1
values=['Python', 'Java', 'C']       # list 2

database=dict(zip(keys,values))      # combining list1 and list 2 to form a dictionary
print(database)

print(database['Anjali'])
# print(database['Arushi'])          # error

database['Arushi']='C++'
print(database)

del database['Anchal']
print(database)

program={'JS':'Atom',  'CS':'VS',  'Python':['Pycharm','Sublime'],  'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(program['JS'])
print(program['Python'])
print(program['Python'][1])
print(program['Java'])               # Java is itself a dictionary
print(program['Java']['JEE'])

