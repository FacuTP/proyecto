from django.shortcuts import render
from aappfamilia.models import Persona
# Create your views here.

def mostrar_familia(request):

    f1= Persona (nombre = "Jorge", sexo = "Masculino", fecha_nacimiento = "21-10-1944")
    f2= Persona (nombre = "Marta", sexo = "Femenino", fecha_nacimiento = "26-01-1952")
    f3= Persona (nombre = "Yamila", sexo = "Femenino", fecha_nacimiento = "10-04-1995")

    return render(request,"C:/Users/Facu/Desktop/programar/proyecto1/nuevo_proyecto1/proyecto/template",{"persona"[f1,f3]})