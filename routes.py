from app import app, db
from flask import render_template, redirect, url_for
import forms #desde forms.py
from models import Task

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
#habilito metod post, ademas del get.
@app.route("/add", methods=["POST","GET"])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        unaTarea = Task(title = form.title.data)
        db.session.add(unaTarea)
        db.session.commit()
        return render_template("add.html", form=form, title=form.title.data)
    return render_template("add.html", form = form)