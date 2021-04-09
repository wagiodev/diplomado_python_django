class Doctor():
    id = ''
    nombre = ''
    documento = ''
    def __init__(self, id, nombre, documento):
        self.id = id
        self.nombre = nombre
        self.documento = documento

    def doctorExiste(self,doctores,document):
        for doctor in doctores:
            if doctor.documento == document:
                return True
            else:
                return False    

