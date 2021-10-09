#Mauricio Colque Morales
from re import template
from flask import Flask, render_template, request

app = Flask(__name__)

datos_personales = []
exp_laboral = []
estudios = []
logros = []
habilidades = []
intereses = []
referencias = []

#Para iniciar las pag2 y pag3 de manera correcta, sin NONE's
estabilizador = []


#Funciones auxiliares para no llenar con valores 'NONE'
def variable_llenada(variable):
    if variable == "": 
        return False
    return True #se llenó

def lista_llenada(lista):
    for elem in lista:
        if elem == "": 
            return False
    return True #se llenó



@app.route("/")
def index():
    global flag_de_cambio
    flag_de_cambio = True

    return render_template("pag1.html")


@app.route("/pag2", methods=["POST"])
def pag2():

    datos = ["nombres", "apellidos", "titulo", "direccion", 
            "ciudad", "pais", "telefono",
            "email", "presentacion", "linkedin"]

    for dato in datos:
        datos_personales.append(request.form.get(dato))

    #Para que los primeros datos no sean 'NONE' 

    if len(estabilizador) == 0:
        estabilizador.append(1)
        return render_template("pag2.html")


    #Estudios
    temporal = [request.form.get("lugar"), request.form.get("estudio"), 
                request.form.get("est_inicio"),  request.form.get("est_fin")]

    if lista_llenada(temporal):
        estudios.append(temporal)

    #Experiencia laboral
    temporal = [request.form.get("accion"), request.form.get("puesto"),
                request.form.get("exp_inicio"), request.form.get("exp_fin")]

    if lista_llenada(temporal):
        exp_laboral.append(temporal)
    
    #Logros
    temporal = request.form.get("logro")
    if variable_llenada(temporal):
        logros.append(temporal)

    return render_template("pag2.html", estudios=estudios, exp_laboral = exp_laboral, logros=logros)

@app.route("/pag3", methods=["POST"])
def pag3():

    if len(estabilizador) == 1:
        estabilizador.append(2)
        return render_template("pag3.html")

    #Habilidades
    temporal = [request.form.get("habilidad"), request.form.get("dominio")]

    if lista_llenada(temporal):
        #Agregar solo en caso haya sido llenada
        habilidades.append(temporal) 

    #Intereses
    temporal = request.form.get("interes")
    if variable_llenada(temporal):
        intereses.append(temporal)
        
    #Referencias
    temporal = [request.form.get("r_email"), request.form.get("r_telefono")]

    if lista_llenada(temporal):
        referencias.append(temporal)

    return render_template("pag3.html", habilidades=habilidades, intereses=intereses, referencias=referencias)


@app.route("/plantilla", methods=["POST"])
def plantilla_cv():
    
    return render_template("cv.html", datos_personales=datos_personales, exp_laboral=exp_laboral, 
                            estudios=estudios, logros=logros, habilidades=habilidades, 
                            intereses=intereses, referencias=referencias )



