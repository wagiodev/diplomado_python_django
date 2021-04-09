from Mysql import Query

class StudentManager():

    def __init__(self):
        self.query = Query()

    def registerNewStudent(self,doc,name):
        query = Query()
        return query.Add(students=None,document=doc,name_student=name)
    
    def loginStudent(self,value):
       query = Query()
       return query.showByField('students','document',value)
    
    def getAsignaturesByStudent(self,id_student):
        query = Query()
        return query.getAsignatureByStudent(id_student)
    
    def getGroups(self):
        query = Query()
        return query.getGroups()
    
    def getGroupByStudent(self,id_group,id_student):
        query = Query()
        return query.getGroupByStudent(id_group,id_student)

    def registerInGroup(self,id_group,id_student):
        query = Query()
        return query.Add(group_students=None,id_group=id_group,id_student=id_student)

    def getCalificationsByGroupStudent(self,id_group,id_student):
        query = Query()
        return query.getCalificationsByGroupStudent(id_group,id_student)
""" student = Query()
print(student.showByField('groups','id_teacher','1')) """
# student.showByDocument('students','document','1234')
""" rows= student.showAll('students')
for row in rows:
   print(row['name_student']) """
# student.Add(teachers=None,document='5555',name_teacher='Yorley Candela')

