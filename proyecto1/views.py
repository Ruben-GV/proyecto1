from django.http import HttpResponse
import datetime
from django.template import Template, context
from django.template import loader

def saludar(request):
    return HttpResponse("Hola Mundo!")

def segunda_vista(request):
    return HttpResponse("Ya entendí, esta muy facil")

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    cadena=f"Hoy es {dia}"
    return HttpResponse(cadena)

def saludo_con_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre} como estas!")

def probandohtml(request):

    diccionario = {"nombre":"Juan", "apellido":"Perez", "edad":25, "lista":[10,5,2,7,8,3,8,10]}

    template=loader.get_template("template1.html")
    
    documento=template.render(diccionario)
    return HttpResponse(documento)