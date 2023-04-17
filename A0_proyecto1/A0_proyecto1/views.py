from django.http import HttpResponse
import datetime

def saludo(request):
    documento = "<html><body><h1>Hola Alumnos... primera página con django!</h1></body></html>";
    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("hasta luego alumnos de django!")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
        <html>
            <body>
                <h1>Fecha y hora actual: %s</h1>
            </body>
        </html>
        """ % fecha_actual;
    return HttpResponse(documento)

def calculaEdad(request, agno):
    edadActual = 18
    periodo = agno - 2019
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(agno, edadFutura)
    return HttpResponse(documento)

def calculaEdad2(request, edad, agno):
    #edadActual = 18
    periodo = agno - 2019
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(agno, edadFutura)
    return HttpResponse(documento)


#-----------------------------------------clase 5 plantillas----------------------------------------------------

#------------------------IMPORT------------------------------------
from django.template import Template, Context
#------------------------------------------------------------

def saludo2(request):

    p1 = Persona("profesor Juan", "Díaz...")

    nombre = "Juan"
    apellido = "Díaz"
    ahora = datetime.datetime.now()

    doc_externo = open("C:/Users/Fanta/Documents/12.-DJANGO/A0_proyecto1/A0_proyecto1/plantillas/A0_5_Plantilla1.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona" : nombre, "apellido_persona" : apellido, "ahora" : ahora, "nombre2" : p1.nombre, "apellido2" : p1.apellido})
    documento = plt.render(ctx)
    return HttpResponse(documento)


#                                          ^
#                                          |
#----------------------6-------------------|
class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido



#-----------------------------------------clase 7 y 8 plantillas----------------------------------------------------

def saludo3(request):

    p1 = Persona("profesor Juan", "Díaz...")

    nombre = "Juan"
    apellido = "Díaz"
    ahora = datetime.datetime.now()
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    temas2 = []

    doc_externo = open("C:/Users/Fanta/Documents/12.-DJANGO/A0_proyecto1/A0_proyecto1/plantillas/A0_5_Plantilla1.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona" : nombre, "apellido_persona" : apellido, "ahora" : ahora, "nombre2" : p1.nombre, "apellido2" : p1.apellido, "temas" : temas, "temas2" : temas2})
    documento = plt.render(ctx)
    return HttpResponse(documento)



#-----IMPORT DE CARGADOR DE PLANTILLAS---------------------------------
from django.template import loader
#------------------------------------------------------------

#------- CLASE 8 ------- USANDO LOADER EN VEZ DE SEÑALAR MANUALMENTE EL PATH DONDE ESTÁ LA PLANTILLA.

# 1 - EN EL ARCHIVO SETTINGS SE ESPECIFICA LA CARPETA DONDE ESTÁN LAS PLANTILLAS. EN TEMPLATES - DIRS.
# 2 - ESPECIFICA LA PLANTILLA Q SE VA A USAR.
# 3 -YA NO SE PASA UN CONTEXT AL METODO RENDER. SINO QUE SE PASA EL DICCIONARIO DIRECTAMETE AL RENDER

def saludo4(request):
    p1 = Persona("profesor Juan", "Díaz...")
    nombre = "Juan"
    apellido = "Díaz"
    ahora = datetime.datetime.now()
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    temas2 = []

    doc_externo = loader.get_template('A0_5_Plantilla1.html')  #2
    #3
    documento = doc_externo.render({"nombre_persona" : nombre, "apellido_persona" : apellido, "ahora" : ahora, "nombre2" : p1.nombre, "apellido2" : p1.apellido, "temas" : temas, "temas2" : temas2})
    return HttpResponse(documento)


#---------------------- CLASE 9 --------------------------------------------------------------

#------------------------IMPORT------------------------------------
from django.shortcuts import render
#------------------------------------------------------------

def saludo5(request):
    p1 = Persona("profesor Juan", "Díaz...")
    nombre = "Juan"
    apellido = "Díaz"
    ahora = datetime.datetime.now()
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    temas2 = []
    return render(request, "A0_5_Plantilla1.html", {"nombre_persona" : nombre, "apellido_persona" : apellido, "ahora" : ahora, "nombre2" : p1.nombre, "apellido2" : p1.apellido, "temas" : temas, "temas2" : temas2})


#---------------------- CLASE 10 ------------HERENCIA DE PLANTILLAS----------------------------

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "A3_10_CursoC.html", {"dameFecha" : fecha_actual})

def cursoCss(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "A4_10_CursoCss.html", {"dameFecha" : fecha_actual})