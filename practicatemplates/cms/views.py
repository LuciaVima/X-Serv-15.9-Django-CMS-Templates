from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.

@csrf_exempt
def index(request, pagina):
	if request.user.is_authenticated():
		respuesta = 'Hola ' + request.user.username + ' <a href="/logout">Logout</a>' + '<br/>'
	else:
		respuesta = 'Por favor, registrate ' + '<a href="/login">login</a>' + '<br/>'
	if request.method == 'GET':
		try:
			listado = Pages.objects.get(name=pagina)
		except Pages.DoesNotExist:
			respuesta += 'Lo sentimos, esta pagina no ha sido almacenada.'
			return HttpResponse(respuesta)
		respuesta += str(listado.page)
	elif request.method == 'PUT':
		if request.user.is_authenticated():
			try:
				listado = Pages.objects.get(name=pagina)
				respuesta += "Esta url ya ha sido incluida, introduzca otra nueva."
			except Pages.DoesNotExist:
				info = request.body
				p = Pages(name=pagina, page=info)
				p.save()
				respuesta += "La url se ha incluido con exito"	
		else:
			respuesta += 'Para poder incluir una pagina nueva debe de estar registrado. Por favor, registrese.'
	return HttpResponse(respuesta)

@csrf_exempt
def pagina(request, indice):
	if request.user.is_authenticated():
		respuesta = 'Hola ' + request.user.username + ' <a href="/logout">Logout</a>' + '<br/>'
	else:
		respuesta = 'Por favor, registrate ' + '<a href="/login">login</a>' + '<br/>'

	if request.method == 'PUT':
		if request.user.is_authenticated():
			respuesta += 'Esta pagina no puede ser almacenada, introduzca una cadena de caracteres valida'
		else:
			respuesta += 'Para poder incluir una pagina nueva debe de estar registrado. Por favor, registrese.'
	else:
		try:
			listado = Pages.objects.get(id=int(indice))
		except Pages.DoesNotExist:
			respuesta += 'Lo sentimos, esta pagina no ha sido almacenada.'
			return HttpResponse(respuesta)
		respuesta += str(listado.page)		
	return HttpResponse(respuesta)

def listado(request):
	if request.user.is_authenticated():
		respuesta = 'Hola ' + request.user.username + ' <a href="/logout">Logout</a>' + '<br/>'
	else:
		respuesta = 'Por favor, registrate ' + '<a href="/login">login</a>' + '<br/>'
	paginas = Pages.objects.all()
	respuesta += "<ol>"
	for pagina in paginas:
		respuesta += '<li><a href="/' + str(pagina.id) + '">' + str(pagina.name) + '</a>'
	respuesta += "</ol>"
	return HttpResponse(respuesta)


def listadoplantilla(request):
	respuesta = listado(request)
	respuesta = respuesta.content
	template = get_template('plantilla.html')
	return HttpResponse(template.render(Context({'contenido': respuesta})))

def paginaplantilla(request, indice):
	respuesta = pagina(request, indice)
	respuesta = respuesta.content
	template = get_template('plantilla.html')
	return HttpResponse(template.render(Context({'contenido': respuesta})))

def indexplantilla(request, pagina):
	respuesta=index(request, pagina)
	respuesta = respuesta.content
	template = get_template('plantilla.html')
	return HttpResponse(template.render(Context({'contenido': respuesta})))



def usuario(request):
	respuesta = "Eres " + request.user.username
	return HttpResponse(respuesta)



