my_lista=['WALTER','YORLEY','LUCAS']
print('LISTA')
print(my_lista)
my_lista.append('PEDRO')
print('LISTA APPEND')
print(my_lista)
my_lista.pop()
print('LISTA POP')
print(my_lista) 


#DICCIONARIO DE DEUDAS
my_diccionario ={
    'energia':40000,
    'agua':35000,
    'gas':10000,
    'internet':50000,
    'television':40000
}

print('items')
print(my_diccionario.items())
print('get')
print(my_diccionario.get('eneregia'))

#tupla
my_tupla=('1','2',my_lista,my_diccionario)
print('tupla')
print(my_tupla)