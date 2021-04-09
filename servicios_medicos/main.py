'''
 Implementar la logica de una institucion educativa.

Profesores
Estudiantes
Materias
Notas
Horarios de Clase (*opcional)
estas entidades deben ser implementadas mediante objetos. el programa debe permitir las siguientes funciones:

1) un profesor debe poder ver las materias que tienen asignadas (un profesor puede dictar varias clases pero debe al menos dar una)

2) Una materia puede ser dictada por varios profesores y pueden estar inscritos varios estudiantes

3) un estudiante puede estar inscritos en muchas materias

4) las notas son ingresadas por el profesor que dicta la materia en la clase donde el estudiante este incrito

5) los estudiantes deben poder ver que notas tienen y ver un promedio por materia y general en todas sus materias

6) {OPCIONAL} - los horarios son definidos de maximo 6 horas diarias, un estudiante no puede estar en dos materias con el mismo horario, un profesor no puede dictar dos materias que sean vistas el mismo

'''
from Doctor import Doctor
from Paciente import Paciente
from Notas import Notas
from Cita import Cita
contador = 0 
names_objects_id = {
}

def populate_data():
    doctores = []
    pacientes = []
    notas = []
    citas = []

    # --- POPUlAMOS DOCTORES ---
    id = autoIncrement('doctores')
    doctor_1 = Doctor(
        id = id,
        nombre = 'Walter Giovanny Cuadros Rincón',
        documento = 908
    )

    id = autoIncrement('doctores')
    doctor_2 = Doctor(
        id = id,
        nombre = 'Raul Castillo',
        documento = 809
    )

    id = autoIncrement('doctores')
    doctor_3 = Doctor(
        id = id,
        nombre = 'Edgar Vivar',
        documento = 980
    )

    id = autoIncrement('doctores')
    doctor_4 = Doctor(
        id = id,
        nombre = 'Janeth Blanco',
        documento = 890
    )

    doctores.append(doctor_1)
    doctores.append(doctor_2)
    doctores.append(doctor_3)
    doctores.append(doctor_4)


    id = autoIncrement('pacientes')
    print('cristian {}'.format(id))
    paciente_1= Paciente(
        id = id,
        nombre = 'Christian Perez',
        documento = 1234
    )

    id = autoIncrement('pacientes')
    paciente_2= Paciente(
        id = id,
        nombre = 'Javier Gonzalez',
        documento = 4567
    )

    id = autoIncrement('pacientes')
    paciente_3= Paciente(
        id = id,
        nombre = 'Omaira Rincón',
        documento = 890
    )

    id = autoIncrement('pacientes')
    paciente_4= Paciente(
        id = id,
        nombre = 'Mary Mancipe',
        documento = 246
    )
    pacientes.append(paciente_1)
    pacientes.append(paciente_2)
    pacientes.append(paciente_3)
    pacientes.append(paciente_4)

    id = autoIncrement('cita')
    cita_1 = Cita(
        id = id,
        id_doctor = doctor_1.id,
        id_paciente = paciente_1.id,
        fecha = '24/04/2021',
        hora = '8' 
    )

    id = autoIncrement('cita')
    cita_2 = Cita(
        id = id,
        id_doctor = doctor_2.id,
        id_paciente = paciente_2.id,
        fecha = '24/04/2021',
        hora = '8' 
    )

    id = autoIncrement('cita')
    cita_3 = Cita(
        id = id,
        id_doctor = doctor_3.id,
        id_paciente = paciente_3.id,
        fecha = '24/04/2021',
        hora = '8'
          
    )

    id = autoIncrement('cita')
    cita_4 = Cita(
        id = id,
        id_doctor = doctor_4.id,
        id_paciente = paciente_4.id,
        fecha = '24/04/2021',
        hora = '8'  
    )

    citas.append(cita_1)
    citas.append(cita_2)
    citas.append(cita_3)
    citas.append(cita_4)
    return {
        'doctores':doctores,
        'pacientes':pacientes,
        'citas':citas,
        'notas':notas
    }


def autoIncrement(name_object):
    if name_object in names_objects_id:
        contador = int(names_objects_id.get(name_object))
    else:
        contador = 0
    contador = contador+1
    names_objects_id[name_object] = contador
    return contador

data = populate_data()
doctores = data.get('doctores')
data_sesion = {}

def inicio():
    print('****************** MENU ***************')
    role = int(input('Digita 0 si eres Doctor o 1 si eres un Paciente'))
    document = int(input('Digita tu número de documento'))
    if role == 0:
        doctores = data.get('doctores')
        doctorExiste = False
        for doctor in doctores:
            if doctor.documento == document:
                doctorExiste = True
                data_sesion['role'] = role
                data_sesion['id'] = doctor.id
                data_sesion['documento'] = doctor.documento
                data_sesion['nombre'] = doctor.nombre 
        if doctorExiste == True:
            welcome()
        else:
            volver = int(input('No estas registrado como doctor,\n digita 0 para registarse ó 1 para salir'))
            if volver == 1:
                inicio()
            else:
                registerDoctor()
    else:
        pacientes = data.get('pacientes')
        pacienteExiste = False
        for paciente in pacientes:
            if paciente.documento == document:
                pacienteExiste = True
                data_sesion['role'] = role
                data_sesion['id'] = paciente.id
                print(paciente.id)
                data_sesion['documento'] = paciente.documento
                data_sesion['nombre'] = paciente.nombre 
        if pacienteExiste == True:
            welcome()
        else:
            volver = int(input('No estas registrado como paciente,\n digita 0 para registarse ó 1 para salir'))
            if volver == 1:
                inicio()
            else:
                registerPaciente()

def welcome():

    print('******************* BIENVENIDO {} *******************'.format(data_sesion.get('nombre')))
    if data_sesion['role'] == 1:
        opcion = int(input('Digite 0 para registrar cita ó 1 para ver Notas de citas'))
        if opcion == 0:
            registerCita()
        else:
            verNotas()
    else:
        opcion = int(input('Digite 0 para registrar nota ó 1 para ver citas asignadas'))
        if opcion == 0:
            registerNotas()
        else:
            verCitas()


def registerDoctor():
    print('***************** Registro Doctor *******************')
    nombre = input('Digita tu nombre')
    documento = int(input('Digita tu documento'))
    doctorExiste = False
    for doctor in doctores:
        if doctor.documento == documento:
            doctorExiste = True
        
    if doctorExiste == False:
        print('ENTRO')
        id = autoIncrement('doctores')
        doctor = Doctor(
            id = id,
            nombre = nombre,
            documento = documento
        )
        data.get('doctores').append(doctor)
        data_sesion['role'] = 0
        data_sesion['id'] = doctor.id
        data_sesion['documento'] = doctor.documento
        data_sesion['nombre'] = doctor.nombre 
        welcome()
    else:
        print('Este doctor ya existe')
        registerDoctor()


def registerPaciente():
    print('***************** Registro Paciente *******************')
    nombre = input('Digita tu nombre')
    documento = int(input('Digita tu documento'))
    pacienteExiste = False
    for paciente in pacientes:
        if paciente.documento == paciente:
            pacienteExiste = True
        
    if pacienteExiste == False:
        print('ENTRO')
        id = autoIncrement('doctores')
        paciente = Paciente(
            id = id,
            nombre = nombre,
            documento = documento
        )
        data.get('pacientes').append(paciente)
        data_sesion['role'] = 0
        data_sesion['id'] = paciente.id
        data_sesion['documento'] = paciente.documento
        data_sesion['nombre'] = paciente.nombre 
        welcome()
    else:
        print('Este paciente ya existe')
        registerPaciente()

def registerCita():
    print('***************** REGISTRO CITA *****************')
    sentence = ''
    for doctor in doctores:
        sentence += 'Digita {} para seleccionar al doctor {},\n'.format(doctor.id,doctor.nombre)
    id_doctor = int(input(sentence))
    fecha= input('Digite la fecha con el siguiente formato d/m/a)')
    hora = input('Digita la hora de la cita (desde las 8 hasta 18 horas, sin minutos ni segundos)')
    disponibilidad_doctor = checkDisponibilidadDoctor(id_doctor,fecha,hora)
    if disponibilidad_doctor == False:
        print('Este doctor no esta disponible para la fecha seleccionada')
        welcome()
    else:
        id = autoIncrement('cita')

        cita = Cita(
            id = id,
            id_paciente = data_sesion['id'],
            id_doctor = id_doctor,
            fecha = fecha,
            hora = hora
        )  
        data.get('citas').append(cita)
        print('CITA REGISTRADA')
        opcion = int(input('Digite 0 para volver al menu o 1 para salir'))
        if opcion == 0:
            welcome()
        else:
            inicio()

def registerNotas():
    print('**************** REGISTRO NOTAS ****************')
    documento_paciente = int(input('Digita el documento del paciente'))
    pacientes = data.get('pacientes')
    id_paciente = ''
    for paciente in pacientes:
        if paciente.documento == documento_paciente:
            id_paciente = paciente.id
    citas = data.get('citas')
    if id_paciente == '':
        print('Paciente no esta registrado')
    sentence = ''
    for cita in citas:
        if cita.id_paciente == id_paciente:
            sentence += 'Digita {} para seleccionar la cita fecha: {}, hora {}'.format(cita.id,cita.fecha,cita.hora)
    if sentence == '':
        print('No hay citas asignadas para este paciente')
        welcome()

    id_cita = int(input(sentence))
    nota = input('Digita la nota de esta cita')
    id = autoIncrement('notas')
    nota = Notas(
        id =id,
        id_cita =id_cita,
        nota = nota
    )
    data.get('notas').append(nota)
    print('Nota registrada')
    opcion = int(input('Digita 0 para volver al menu anterior \nó 1 para cambiar de rol'))
    if opcion == 0:
        welcome()
    else:
        inicio() 

def checkDisponibilidadDoctor(id_doctor, fecha, hora):
    #Para efectos academicos se supone que cada cita dure una hora
    contador = 0
    citas = data.get('citas')
    for cita in citas:
        if cita.hora == hora:
            return False
        if cita.id_doctor == id_doctor and cita.fecha == fecha: 
            contador = contador + 1
        
    if contador >= 3:
        disponible = False
    else:
        disponible = True
    return disponible
    
def verNotas():
    print('*********** VER NOTAS ***********')
    citas = data.get('citas')
    notas = data.get('notas')
    print_notas = ''
    for cita in citas:
        if cita.id_paciente == data_sesion['id']:
            for nota in notas:
                if cita.id == nota.id_cita:
                    print_notas += '{} -> {}\n'.format(cita.fecha,nota.nota)
    if print_notas == '':
        welcome()
    print(print_notas)
    opcion = int(input('Digita 0 para volver al menu anterior \nó 1 para cambiar de rol'))
    if opcion == 0:
        print('No hay notas para mostrar')
        welcome()
    else:
        inicio()

def verCitas():
    print('*********** VER CITAS ************')
    citas = data.get('citas')
    doctores = data.get('doctores')
    sentence =''
    print(data_sesion)
    for cita in citas:

        print('cita.id_doctor {}'.format(cita.id_doctor))
        if cita.id_doctor == data_sesion['id']:
            for doctor in doctores:
                print('doctor.id {}'.format(doctor.id))
                if doctor.id == data_sesion['id']:
                    sentence += 'Fecha: {}, hora: {}, paciente: {} '.format(cita.fecha,cita.hora,doctor.nombre)
    print(sentence)
    opcion = int(input('Digita 0 para volver al menu anterior \nó 1 para cambiar de rol'))
    if opcion == 0:
        welcome()
    else:
        inicio()    

inicio()

