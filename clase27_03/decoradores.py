def prevet_error(f):
    def wrapper(*args, **kwargs):
        try:
          f(*args, **kwargs)
        except: 
          print('ocurrio un error')
    return wrapper


@prevet_error
def dummy_code(nota_1, nota_2):
  prom = nota_1 + nota_2 /nota_2
  print(prom)
print('DIVISION EN CERO')
dummy_code(5, 0)

@prevet_error
def saludar_personas(personas):
    nombre = personas.get('nombre')
    edad = personas['edad']
    profesion = personas.get('profesion')
    return 'Hola mi nombre es: {nombre}, tengo {edad}, profesion {profesion}'.format(nombre=nombre,edad=edad,profesion=profesion)

personas = [ {
        'nombre':'Walter',
        'edad':'27'
          
    },
    {
        'nombre':'Yorley',
        'edad':'25'
        
    }
]

print('PARAMETRO EN NULL')
for persona in personas:
    print(saludar_personas(None))

print('OMITIENDO PARAMETRO EN DICCIONARIO')
for persona in personas:
    print(saludar_personas(personas))
@prevet_error
def imprimir_lista(lista):
  print(lista[5])

print('PARAMETRO INDEX')
lista= ['Walter','Giovanny']
imprimir_lista(lista)