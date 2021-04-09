
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import date

class Query():        
    '''
    This class containt all querys to the bd
    '''
    def __init__(self):
        self.myCon = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="universidad_walter")

    '''

    This function is for get data of a query with a clause
    
    '''
    def showByField(self, nameTable, field, value):

      mycursor = self.myCon.cursor(dictionary=True)
      
      mycursor.execute("SELECT * FROM {}  WHERE {} ='{}'".format(nameTable,field,value))
     
      myRecordset = mycursor.fetchone()
      """ for r in myRecordset:
        result = r
      mycursor.close() """
      return myRecordset

    '''
    This function get all data of the bd table
    '''
    def showAll(self,nameTable): 
        mycursor = self.myCon.cursor(dictionary=True)
      
        mycursor.execute("SELECT * FROM {}".format(nameTable))
     
        myRecordset = mycursor.fetchall()
        
        """ for r in myRecordset:
            print(r[0], r[1])
        mycursor.close() """
        mycursor.close() 
        return myRecordset

    '''
    Get asignatures by id of a student
    '''
    def getAsignatureByStudent(self,id_student):
        mycursor = self.myCon.cursor(dictionary=True)

        sql = "SELECT \
        group_students.id_group , \
        asignatures.id AS id_asignature, \
        asignatures.name_asignature \
        FROM group_students \
        INNER JOIN groups ON group_students.id_group = groups.id \
        INNER JOIN asignatures ON groups.id_asignature = asignatures.id\
        WHERE group_students.id_student ={}".format(id_student)

        
        mycursor.execute(sql)
        
        myRecordset = mycursor.fetchall()
        """ for r in myRecordset:
            result = r
        mycursor.close() """
        return myRecordset
    
    '''
    Get all a groups, a group is a table where it relates subjects with teachers
    '''
    def getGroups(self):
        mycursor = self.myCon.cursor(dictionary=True)

        sql = "SELECT \
        groups.id, \
        groups.id_asignature, \
        groups.id_teacher, \
        asignatures.name_asignature, \
        teachers.name_teacher \
        FROM groups \
        INNER JOIN asignatures ON groups.id_asignature = asignatures.id \
        INNER JOIN teachers ON groups.id_teacher = teachers.id"

        
        mycursor.execute(sql)
        
        myRecordset = mycursor.fetchall()
        """ for r in myRecordset:
            result = r
        mycursor.close() """
        return myRecordset

    '''
    Get one group
    '''
    def getGroupByStudent(self,id_group,id_student):
        mycursor = self.myCon.cursor(dictionary=True)

        sql = "SELECT \
        group_students.id_student, \
        group_students.id, \
        group_students.id_group, \
        asignatures.name_asignature, \
        students.name_student \
        FROM group_students \
        INNER JOIN groups ON group_students.id_group = groups.id \
        INNER JOIN asignatures ON groups.id_asignature = asignatures.id \
        INNER JOIN students ON group_students.id_student = students.id \
        WHERE group_students.id_group = {} \
        AND group_students.id_student = {} ".format(id_group,id_student)

        
        mycursor.execute(sql)
        
        myRecordset = mycursor.fetchall()
        """ for r in myRecordset:
            result = r
        mycursor.close() """
        return myRecordset

    '''
    Get group by id of a teacher
    '''
    def getGroupByTeacher(self,id_teacher=""):
        mycursor = self.myCon.cursor(dictionary=True)

        sql = "SELECT \
        groups.id as id_group, \
        groups.id_asignature, \
        groups.id_teacher, \
        asignatures.name_asignature, \
        teachers.name_teacher \
        FROM groups \
        INNER JOIN asignatures ON groups.id_asignature = asignatures.id \
        INNER JOIN teachers ON groups.id_teacher = teachers.id \
        WHERE groups.id_teacher = {}".format(id_teacher)

        
        mycursor.execute(sql)
        
        myRecordset = mycursor.fetchall()
        """ for r in myRecordset:
            result = r
        mycursor.close() """
        return myRecordset

    '''
    Get one group by id teacher and by id asignature
    '''
    def getOneGroupByTeacher(self,id_asignature,id_teacher):
        mycursor = self.myCon.cursor(dictionary=True)

        sql = "SELECT \
        groups.id_asignature, \
        groups.id_teacher, \
        asignatures.name_asignature, \
        teachers.name_teacher \
        FROM groups \
        INNER JOIN asignatures ON groups.id_asignature = asignatures.id \
        INNER JOIN teachers ON groups.id_teacher = teachers.id \
        WHERE groups.id_teacher = {} \
        and groups.id_asignature = {}".format(id_teacher,id_asignature)

        
        mycursor.execute(sql)
        
        myRecordset = mycursor.fetchall()
        """ for r in myRecordset:
            result = r
        mycursor.close() """
        return myRecordset
    '''
    Get all students by group, and get asignatures by teacher
    '''
    def getStudentsByGroup(self,id_group):
        mycursor = self.myCon.cursor(dictionary=True)

        sql = "SELECT \
        group_students.id_student, \
        group_students.id, \
        group_students.id_group, \
        students.name_student \
        FROM group_students \
        INNER JOIN groups ON group_students.id_group = groups.id \
        INNER JOIN asignatures ON groups.id_asignature = asignatures.id \
        INNER JOIN students ON group_students.id_student = students.id \
        WHERE group_students.id_group = {}".format(id_group)

        
        mycursor.execute(sql)
        
        myRecordset = mycursor.fetchall()
        """ for r in myRecordset:
            result = r
        mycursor.close() """
        return myRecordset

    '''
    Get calification by id group and id student
    '''
    def getCalificationsByGroupStudent(self,id_group,id_student):
        mycursor = self.myCon.cursor(dictionary=True)

        sql = "SELECT \
        califications.id_student, \
        califications.id, \
        califications.id_group, \
        califications.value, \
        asignatures.name_asignature \
        FROM califications \
        INNER JOIN groups ON califications.id_group = groups.id \
        INNER JOIN asignatures ON groups.id_asignature = asignatures.id \
        WHERE califications.id_group = {} \
        AND califications.id_student = {} ".format(id_group,id_student)

        
        mycursor.execute(sql)
        
        myRecordset = mycursor.fetchall()
        """ for r in myRecordset:
            result = r
        mycursor.close() """
        return myRecordset
    '''
    This a generic function for save rows in a bd
    '''
    def Add(self,**kwargs):
        try:
            mycursor = self.myCon.cursor()     
            
            """ today=date.today()
            tdate = today.strftime("%Y/%d/%m")
            #date_time=datetime.datetime.now()
            print(tdate) """
            fields=""
            values=""
            i = 0
            for key, value in kwargs.items():
                if i== 0:
                    query = "insert into {}".format(key)
                elif i == 1:
                    fields += "{}".format(key)
                    values += "'{}'".format(value)
                else:
                    fields += ",{}".format(key)
                    values += ",'{}'".format(value)
                i += 1
            query_insert = query+" ("+fields+") values ("+values+");"
            mycursor.execute(query_insert)
            self.myCon.commit()
            return True
        
        except mysql.connector.Error as error:
            print("Failed to insert query into table {}".format(error))
        finally:
            mycursor.close()

