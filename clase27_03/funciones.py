
def saluda(nombre_persona):
    print('HOLA {nombre_persona}'.format(nombre_persona=nombre_persona))


def promedio(data):
    mean = sum(data)/len(data)
    print(mean)


lista=[1,2,3,4,5,6,7,8,9]
nombre_persona = 'Walter Cuadros'
print('FUNCION SALUDA')
saluda(nombre_persona)
print('Funcion promedio')
promedio(lista)

personas = [ {
        'nombre':'Walter',
        'edad':'27',
        'profesion':'Ingeniero Electrónico'    
    },
    {
        'nombre':'Yorley',
        'edad':'25',
        'profesion':'docente'
    }
]
def saludar_personas(personas):
    nombre = personas.get('nombre')
    edad = personas.get('edad')
    profesion = personas.get('profesion')
    return 'Hola mi nombre es: {nombre}, tengo {edad}, profesion {profesion}'.format(nombre=nombre,edad=edad,profesion=profesion)


for persona in personas:
    print(saludar_personas(persona))