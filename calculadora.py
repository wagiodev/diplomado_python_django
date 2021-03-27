print('Hola cual es tu nombre')
nombre = input()
print('Por favor digita el primer numero')
a = int(input())
print('Por favor digita el segundo número')
b = int(input())
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    return a/b

def potencia(a,b):
    return a+b

def saludar(nombre):
    return "chao"+nombre

c = suma(a,b)
print('sumar: '+str(c))

c = resta(a,b)
print('resta: '+str(c))

c = multiplica(a,b)
print('multiplica: '+str(c))

c = divide(a,b)
print('divide: '+str(c))

c = potencia(a,b)
print('potencia: '+str(c))

saludar(nombre)