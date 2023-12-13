from django.shortcuts import render
from hospital.models import Hospital, Doctor, Empleado

def index(request):
    return render(request, 'hosp/index.html')

def hosps(request):
    hosp = Hospital()
    listaHospitales = hosp.lista()
    contexto = {
        'listado_Hospitales': listaHospitales
    }
    return render(request, 'hosp/hospitales.html', contexto)

def docs(request):
    doc = Doctor()
    listaDoctores = doc.lista()
    contexto = {
        'listado_Doctores': listaDoctores
    }
    return render(request, "hosp/doctores.html", contexto)

def emps(request):
    emp = Empleado()
    listaEmpleados = emp.lista()
    contexto = {
        'listado_Empleados': listaEmpleados
    }
    return render(request, "hosp/empleados.html", contexto)