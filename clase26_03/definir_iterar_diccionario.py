print('VAMOS A CREAR NUESTRO LISTADO DE REPUESTOS')
repuestos = {}
isOk = True
while isOk:
    print('Ingresa el nombre del repuesto')
    nombre = input()
    print('Ingresa el precio del repuesto')
    precio = int(input())
    repuestos[nombre]=precio
    print('Oprima 0 si desea agregar otro repuesto, o cualquier número si desea salir')
    a = int(input())
    isOk = isContinue(a)
    
isOk = True
my_list = []
while isOk:
    print('Ingresa el nombre que deseas escoger')
    nombre = input()
    my_list.append(nombre)
    print('Oprima 0 si desea escoger más repuestos de la lista, o cualquier número si desea salir')
    a = int(input())
    isOk = isContinue(a)
    
pago_total = 0
print(my_list)
for key,value in repuestos.items():
    print(key)
    if key in my_list:
        pago_total=pago_total+value


print('El valor total a pagar es:'+str(pago_total))

def isContinue(a):
    if a>0:
        return False
    else:
        return True
