
class Profesor():
    id = ''
    nombre = ''
    
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def get_materias(self, matriculas):
        list_matricula = []
        for matricula in matriculas:
            if matricula.id == self.id:
                list_matricula.append(matricula)
        return list_matricula