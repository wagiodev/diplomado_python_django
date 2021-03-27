my_list= my_lista=['WALTER','YORLEY','LUCAS','PEDRO','GIOVANNY']
print('Resultado iterar lista')
for i in my_list:
    print (i)
print('Resultado iterar lista con range')
for i in range(len(my_list)):
    print(i)

the_dictionary ={
    'matematicas':100,
    'español':94,
    'ciencias':50,
    'informatioca':100,
    'fisica':95
}

print('Resultado iterar  diccionario')
for key in the_dictionary.keys():
    print(key)

print('Resultado iterar lista con range')
for value in the_dictionary.values():
    print(value)

print('Resultado iterar lista con range')
for key in the_dictionary.keys():
    print(key,':',the_dictionary.get(key))

    