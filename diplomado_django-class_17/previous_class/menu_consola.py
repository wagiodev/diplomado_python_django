import random
numero_seleccionado = random.randrange(1,11)
print(numero_seleccionado)
a = 1 
while (a):
  print('Vamos a jugar a adivinar el numero del 1 al 10: ')
  try:
    numero_ingresado = int(input('ingresa el dato: '))
    if numero_seleccionado == numero_ingresado:
      print('adivinaste !! ')

      valor_ingresado = int(input('jugar de nuevo 1, salir 0'))
      if valor_ingresado == 0:
        a = None 
        
      numero_seleccionado = random.randrange(1,11)

  except:
    pass

