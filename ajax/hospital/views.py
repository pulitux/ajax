from django.shortcuts import render
from hospital.models import Hospital, Doctor, Empleado

def index(request):
    return render(request, 'index.html')

def hosps(request):
    hosp = Hospital()
    listaHospitales = hosp.lista()
    contexto = {
        'listado_Hospitales': listaHospitales
    }
    return render(request, 'hospitales.html', contexto)

def docs(request):
    doc = Doctor()
    listaDoctores = doc.lista()
    contexto = {
        'listado_Doctores': listaDoctores
    }
    return render(request, "doctores.html", contexto)

def emps(request):
    emp = Empleado()
    listaEmpleados = emp.lista()
    contexto = {
        'listado_Empleados': listaEmpleados
    }
    return render(request, "empleados.html", contexto)