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
    #cuando levante index carga task desde la base de datos.
    tasks = Task.query.all()

    #return "<h1>Bienvenidos!</h1>"
    #render template busca por defecto en el directorio templates.
    #return render_template("index.html")
    #ahora - enviamos variables para que index.html las procese...
    # mediante jinja
    return render_template("index.html", tasks = tasks)
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
        #luego de importar redirect y url_for en vez de
        #renderizar la plantilla hago un redirect.
        return redirect(url_for('index') )
    return render_template("add.html", form = form)