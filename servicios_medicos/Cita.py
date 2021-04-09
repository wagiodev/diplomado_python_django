class Cita():
    id = ''
    id_paciente = ''
    id_doctor = ''
    fecha = ''
    hora = ''
    def __init__(self, id, id_paciente, id_doctor, fecha, hora):
        self.id = id
        self.id_paciente = id_paciente
        self.id_doctor = id_doctor
        self.fecha = fecha
        self.hora = hora

