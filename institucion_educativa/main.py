from teacher_manager import TeacherManager 
from student_manager import StudentManager

teacher_manager = TeacherManager()
student_manager = StudentManager()
data_session = {}

def prevet_error(f):
    def wrapper(*args, **kwargs):
        try:
          f(*args, **kwargs)
        except: 
            print('Se presentó un error vuelve a correr el programa')
    return wrapper

@prevet_error
def start():
    print('******************Bienvenido********************')
    role = int(input('Selecciona 0 si eres profesor ó 1 si eres estudiante'))
    register = int(input('\nDigita 0 si deseas registrarte ó 1 si deseas hacer login'))
    data_session['role'] = role
    if(register == 1):
        document = input('Digita tu número de documento')
        if role == 0:
            result = teacher_manager.loginTeacher(document)
            if result == None:
                print('El usuario no existe')
                start()
            for key,value in result.items():
                data_session[key] = value
            welcome_teacher()
        else:
            result = student_manager.loginStudent(document)
            if result == None:
                print('El usuario no existe')
                start()
            for key,value in result.items():
                data_session[key] = value
            welcome_student()
    else:
        if role == 0:
            register_teacher()
        else:
            register_student()


def welcome_teacher():
    if len(data_session) > 0:
        print('\n **************** Hola docente '+ data_session.get('name_teacher')+ ' ****************')
        var = int(input('\n Digita 0 si desea registrarse en una materia ó 1 si desea registrar una calificación'))
        if var == 0:
            register_asignature_teacher()
        else:
            register_calification()


def register_teacher():
    print('****************** REGISTRO DE NUEVO DOCENTE ******************')
    document = input('Digita tu número de documento')
    name_teacher = input('Digita tu nombre completo')
    teacherChecked = teacher_manager.loginTeacher(document)
    if teacherChecked == None:
        registerTeacher = teacher_manager.registerNewTeacher(document,name_teacher)
        if registerTeacher == True:
            result = teacher_manager.loginTeacher(document)
            for key,value in result.items():
                data_session[key] = value
            welcome_teacher()
        else:
            print('No fue posible hacer el registro')

    else:
        print('Este docente ya existe en el sistema')
        register_teacher()


def viewAsignatureTeacher():
    asignatures_by_teacher = {}
    rows = teacher_manager.getAsignaturesByTeacher(data_session.get('id'))
    if len(rows) > 0:
        print('****************** Tienes asignadas las siguientes materias ****************** ')
        for row in rows:
            asignatures_by_teacher[row['name_asignature']] = row['id_asignature']
            print(row['name_asignature'])
    else:
        print('No tienes asignadas materias')
        asignatures_by_teacher = {}


def register_asignature_teacher():
    viewAsignatureTeacher()
    rows = teacher_manager.getAsignatures()
    sentence = ""
    for row in rows:
        sentence += 'Digita {} para registrarse en {} \n '.format(row['id'],row['name_asignature'])
    asignatureForRegister = int(input(sentence))
    asignatureCheck = teacher_manager.getOneGroupByTeacher(asignatureForRegister,data_session.get('id'))
    if len(asignatureCheck) == 0:
        registerAsignatureByTeacher = teacher_manager.registerAsignatureByTeacher(asignatureForRegister,data_session.get('id'))
        if registerAsignatureByTeacher == True:
            print('Se ha registrado la materia con exito')
            viewAsignatureTeacher()
        again = int(input('Digita 0 para ingresar otra materia ó 1 para regresar al menu'))
        if again == 1:
            welcome_teacher()
        else:
            register_asignature_teacher()
    else:
        back = int(input('Esta materia ya esta registrada, digita 0 para probar con otra materia  ó 1 para volver al menu'))

        if back == 1:
            welcome_teacher()
        else:
            register_asignature_teacher()
   
def register_calification():
    rows = teacher_manager.getAsignaturesByTeacher(data_session.get('id'))
    sentence = ""
    print('****************** ******************' )
    if len(rows) > 0:
        for row in rows:
            sentence += 'Digita {} para mostrar estudiantes de {} \n '.format(row['id_group'],row['name_asignature'])
        id_group = int(input(sentence))
        rows = teacher_manager.getStudentsByGroup(id_group)
        sentence = ""
        if len(rows)>0:
            for row in rows:
                sentence += 'Digita {} para registrar nota a {} \n '.format(row['id_student'],row['name_student'])
            id_student = int(input(sentence))
            value = float(input('Digite la nota a registrar'))
            registerCalification = teacher_manager.registerCalification(id_group,id_student,value)
            if registerCalification == True:
                print('Se ha registrado la calificación con exito')
            again = int(input('Digita 0 para ingresar otra calificacion ó 1 para regresar al menu'))
            if again == 1:
                welcome_teacher()
            else:
                register_calification()
        else:
            back = int(input('No hay estudiantes registrados para esta materia, digita 0 para probar con otra materia  ó 1 para volver al menu'))
            if back == 1:
                welcome_teacher()
            else:
                register_calification()
    else:
        print('No hay materias registradas para usted')
        welcome_teacher()


def welcome_student():
    if len(data_session) > 0:
        print('\n **************** Hola estudiante '+ data_session.get('name_student')+ ' ****************')
        var = int(input('\n Digita 0 si desea registrarse en una materia ó 1 si desea ver sus calificaciónes'))
        if var == 0:
            register_asignature_student()
        else:
            view_calification_student()

     
def register_student():
    print('****************** REGISTRO DE NUEVO ESTUDIANTE ******************')
    document = input('Digita tu número de documento')
    name_student = input('Digita tu nombre completo')
    studentChecked = student_manager.loginStudent(document)
    if studentChecked == None:
        registerStudent = student_manager.registerNewStudent(document,name_student)
        if registerStudent == True:
            result = student_manager.loginStudent(document)
            for key,value in result.items():
                data_session[key] = value
            welcome_student()
        else:
            print('No fue posible hacer el registro')

    else:
        print('Este estudiante ya existe en el sistema')
        register_student()

def view_asignatures_student():
    asignatures_by_student = {}

    rows = student_manager.getAsignaturesByStudent(data_session.get('id'))
    if len(rows) > 0:
        print('****************** Tienes registradas las siguientes materias ****************** ')
        for row in rows:
            asignatures_by_student[row['name_asignature']] = row['id_group']
            print(row['name_asignature'])
    else:
        print('No tienes registradas materias')
        asignatures_by_student = {}

def register_asignature_student():
    view_asignatures_student()
    rows = student_manager.getGroups()
    if len(rows)>0:
        sentence = ""
        for row in rows:
            sentence += 'Digita {} para registrarse en {} con el docente {} \n'.format(row['id'],row['name_asignature'],row['name_teacher'])
        id_group = int(input(sentence))
        print(data_session)
        groupCheck = student_manager.getGroupByStudent(id_group,data_session.get('id'))
        if len(groupCheck) == 0:
            registerInGroup = student_manager.registerInGroup(id_group,data_session.get('id'))
            if registerInGroup == True:
                print('Se ha registrado la materia con exito')
                view_asignatures_student()
            again = int(input('Digita 0 para registrarse en otro grupo ó 1 para regresar al menu'))
            if again == 1:
                welcome_student()
            else:
                register_asignature_student()
        else:
            back = int(input('Ya estas registrado en este grupo, digita 0 para probar con otra grupo  ó 1 para volver al menu'))

            if back == 1:
                welcome_student()
            else:
                register_asignature_student()

    else:
        print('No hay grupos registrados en este momento')
        welcome_student()


def view_calification_student():

    rows = student_manager.getAsignaturesByStudent(data_session.get('id'))
    print('**************** VER LAS NOTAS POR MATERIA **********************')
    sentence =""
    if len(rows):
        for row in rows:
            sentence += 'Digita {} para ver las notas de {} \n'.format(row['id_group'],row['name_asignature'])
        id_group = int(input(sentence)) 
        
        rows = student_manager.getCalificationsByGroupStudent(id_group,data_session.get('id'))
        if len(rows)>0:
            i = 0
            sumNotes = 0 
            for row in rows:
                i = i+1
                print('{}. Materia {}, calificacion:  {}'.format(i,row['name_asignature'],row['value']))
                sumNotes += float(row['value'])
                name_asignature = row['name_asignature']
            avgNotes = sumNotes/i
            print('Su promedio en {} es de {}'.format(name_asignature,avgNotes))
            again = int(input('Digite 0 para consultar las notas de otra materia ó 1 para volver al menu'))
            if again == 0:
                view_calification_student()
            else:
                welcome_student()
        else:
            again = int(input('No hay notas asignadas para esta materia, digita 0 para intentar de nuevo ó 1 para ir al menu'))
            if again == 0:
                view_calification_student()
            else:
                welcome_student()
    else: 
        again = int(input('No hay calificaciones para esta mataeria,\nDigita 0 para ver las notas de otra materia, \n ó 1 para volver al menu'))
        if again == 1:
            welcome_student()
        else:
            view_calification_student()
def clear_data():
    data_session = {}
start()




