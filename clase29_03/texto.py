'aca esta mi "texto"  some'

"aca tambien 'esta' el texto"

''' 
aca esta otro 'tipo' de texto 
'''

"""
aca esta otro texto
"""


email = 'some@mail.com'
"select * from user where email = '{}';".format(email)

def get_sql_user_by_email(email):
  '''
  Get sql query to get users by email
  :params email String, email to filter user Ie. 'some@mail.com'
  return "select * from user where email = 'some@mail.com';"
  ''' 

  sql = "select * from user where email = '{}';".format(email)
  return sql


get_sql_user_by_email('edgar@mail.com')

```select * from user where email = 'some@mail.com' ;```

def my_func(my_var):
  '''
  do some thing
  :params my_var Int, este para hace algo Ie. 1
  retun 2
  '''

  return my_var +1 

a = 'a'
type(a)

'hola mundo'.capitalize()
'Hola Mundo'.lower()

'Hola Mundo'.upper()
## swapcase() 


'Hola Mundo'.swapcase()

# Métodos de separación y unión


## split(), 


"Hola mundo!\nHello world!".split()

"walter,walters,cuadros".split(',')

"walter,walters,cuadros".split('y')

"walter@walters@cuadros".split('@')

## join(), 


 " ".join(["Hola", "mundo"])

def definicion_join_por_walter(lista):
  separador = ' '
  texto_final = ''
  for i in lista:
    texto_final = texto_final + separador + i
  return texto_final[1:]

lista = ["Hola", "mundo"]
respuesta = definicion_join_por_walter(lista)
print(respuesta)

texto_final

respuesta[3:8]

nombre_completo = 'Juan Sebastián Rodríguez Laverde'
for i in nombre_completo.split():
  print(i)

