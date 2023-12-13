from django.db import models
import cx_Oracle

class Hospital:
    def __init__(self):
        self.connection = cx_Oracle.connect(user='system', password='pythonoracle', dsn='localhost/XE')

    def lista(self):
        lista = []
        cursor = self.connection.cursor()
        consulta = 'SELECT * FROM HOSPITAL ORDER BY HOSPITAL_COD'
        cursor.execute(consulta)
        for row in cursor:
            id, name, dir, tel, beds = row
            lista.append({'id': id, 'name': name, 'dir': dir, 'tel': tel, 'beds': beds})
        return lista

class Doctor:
    def __init__(self):
        self.connection = cx_Oracle.connect(user='system', password='pythonoracle', dsn='localhost/XE')

    def lista(self):
        lista = []
        cursor = self.connection.cursor()
        consulta = 'SELECT * FROM DOCTOR ORDER BY DOCTOR_NO'
        cursor.execute(consulta)
        for row in cursor:
            hosp, id, name, esp, sal = row
            lista.append({'hosp': hosp, 'id': id, 'name': name, 'esp': esp, 'sal': sal})
        return lista

class Empleado:
    def __init__(self):
        self.connection = cx_Oracle.connect(user='system', password='pythonoracle', dsn='localhost/XE')

    def lista(self):
        lista = []
        cursor = self.connection.cursor()
        consulta = 'SELECT * FROM EMP ORDER BY EMP_NO'
        cursor.execute(consulta)
        for row in cursor:
            print (row)
            id, name, job, sup, alta, sal, com, dept = row
            lista.append({'id': id, 'name': name, 'job': job, 'sup': sup, 'alta': alta, 'sal': sal, 'com': com, 'dept': dept})
        return lista
