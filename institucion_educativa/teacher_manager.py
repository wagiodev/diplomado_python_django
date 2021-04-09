from Mysql import Query

class TeacherManager():

    def __init__(self):
        self.query = Query()

    def registerNewTeacher(self,doc,name):
        query = Query()
        return query.Add(teachers=None,document=doc,name_teacher=name)
    
    def loginTeacher(self,value):
        query = Query()
        return query.showByField('teachers','document',value)
    
    def getAsignaturesByTeacher(self,id_teacher):
        query = Query()
        return query.getGroupByTeacher(id_teacher)
    
    def getOneGroupByTeacher(self,id_asignature,id_teacher):
        query = Query()
        return query.getOneGroupByTeacher(id_asignature,id_teacher)

    def getAsignatures(self):
        query = Query()
        return query.showAll('asignatures')

    def registerAsignatureByTeacher(self,id_asignature,id_teacher):
        query = Query()
        return query.Add(groups=None,id_asignature=id_asignature,id_teacher=id_teacher)

    def getStudentsByGroup(self,id_group):
        query = Query()
        return query.getStudentsByGroup(id_group)

    def registerCalification(self,id_group,id_student,value):
        query = Query()
        return query.Add(califications=None,id_group=id_group,id_student=id_student,value=value)

""" student = Query()
print(student.showByField('groups','id_teacher','1')) """
# student.showByDocument('students','document','1234')
# student = Query()
# rows= student.showAll('asignatures')
# for row in rows:
#    print(row['name_asignature'])
# student.Add(teachers=None,document='5555',name_teacher='Yorley Candela')

