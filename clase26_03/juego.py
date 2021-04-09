from random import randint, uniform,random
numero =  randint(0,100)
print('BIENVENIDO TRATA DE ADIVINAR EL NÚMERO')
isWin = False
count = 1
while isWin == False:
    print('Por favor digita un número')
    try:

        a = int(input())
        if a>numero:
            print('Digita un número más pequeño')
        elif a < numero:
            print('Digita un número más grande')
        elif a == numero:
            isWin = True
            print('GANASTE')
        
        count = count+1
    except:
        pass

print('TUVISTE: '+str(count)+' intentos')
    