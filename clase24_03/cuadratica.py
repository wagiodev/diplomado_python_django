import math

print('Bienvenido')
print('Por favor digita el primer numero')
a = float(input())
print('Por favor digita el segundo número')
b = float(input())
print('Por favor digita el tercer número')
c = float(input())
def cuadratica(a,b,c):
   d = (-b + pow((pow(b,2)-(4*a*c)),1/2))/(2*a)
   e = (-b - pow((pow(b,2)-(4*a*c)),1/2))/(2*a)
   li=[]
   li.append(d)
   li.append(e)
   return print(li)

cuadratica(a,b,c)