from app import app
from flask import render_template
import forms #desde forms.py

#cada ruta define una función
#y es lo que se ve de afuera como una pagina.
#si dos rutas van delante de una función,
#entonces ambas ejecutan la misma...
@app.route("/")
@app.route("/index")
def index():
    #return "<h1>Bienvenidos!</h1>"
    #render template busca por defecto en el directorio templates.
    #return render_template("index.html")
    #ahora - enviamos variables para que index.html las procese...
    # mediante jinja
    return render_template("index.html", una_variable_cualquiera="juan paco pedro de la mar")
#testear flask:
#desde terminal ejecutar
# flask run 
# automaticamente buscará en el directorio de trabajo al archivo app.py
@app.route("/chau")
@app.route("/adios")
@app.route("/bye")
def bye():
    #return "Hasta luego!"
    return render_template("test2.html")

@app.route("/add")
def add():
    form = forms.AddTaskForm()
    return render_template("add.html", form = form)