from flask import Flask
#para no cargar todo el html en el codigo python
#se utiliza el render_template.
from flask import render_template

app = Flask(__name__)

#cada ruta define una función
#y es lo que se ve de afuera como una pagina.
#si dos rutas van delante de una función,
#entonces ambas ejecutan la misma...
@app.route("/")
@app.route("/index")
def index():
    #return "<h1>Bienvenidos!</h1>"
    return render_template("index.html")
#testear flask:
#desde terminal ejecutar
# flask run 
# automaticamente buscará en el directorio de trabajo al archivo app.py
@app.route("/chau")
def bye():
    return "Hasta luego!"

if __name__ == "__main__":
    #pass
    app.run(debug=True)