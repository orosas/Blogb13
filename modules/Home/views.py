from django.shortcuts import render
from django.http import HttpResponse

# Create your view here.

def Index(request):
	return render(request,'Home/index.html')

def Contacto(request):
	return HttpResponse('Pagina de contactos')

def Otros(request,num):
	return HttpResponse('Pagina de otros con el numero:  <b> '+num+'</b>')

def Sumar(request,num1, num2):

	lasuma = num1 + num2
	return HttpResponse('La suma de: '+num1+' y '+num2+' es ='+lasuma )

def Saludo(request,nombre):

	return HttpResponse('Hola '+nombre )

def Mayorque(request, num1, num2):
	if num1 > num2:
		return HttpResponse('Parametro 1: '+num1+' mayor que Parametro 2'+num2)
	else:
		return HttpResponse('Parametro 2: '+num2+' mayor que Parametro 1'+num1)