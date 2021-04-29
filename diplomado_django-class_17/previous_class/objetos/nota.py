
class Nota():
    matricula_id = ''
    valor = ''
    
    def __init__(self, matricula_id, valor):     
        self.matricula_id = matricula_id
        self.valor = valor

class Matricula():

    def __init__(self, id, estudiante_id, materia_id, profesor_id):
        self.id = id
        self.estudiante_id = estudiante_id
        self.materia_id = materia_id
        self.profesor_id = profesor_id

    def get_promedio(self, notas):
        suma_notas = 0
        contador_notas = 0
        for nota in notas:
            if nota.matricula_id == self.id:
                suma_notas = suma_notas + nota.valor
                contador_notas = contador_notas + 1
        
        return suma_notas/contador_notas if contador_notas else contador_notas

    def get_mateia(self, materias):
        mi_materia = None
        for materia in materias:
            if materia.id == self.materia_id:
                mi_materia = materia
        
        return mi_materia

    def get_estudiante(self, estudiantes):
        mi_estudiante = None
        for estudiante in estudiantes:
            if estudiante.id == self.estudiante_id:
                mi_estudiante = estudiante
        
        return mi_estudiante
    
    def get_profesor(self, profesores):
        mi_profesor = None
        for profesor in profesors:
            if profesor.id == self.profesor_id:
                mi_profesor = profesor
        
        return mi_profesor