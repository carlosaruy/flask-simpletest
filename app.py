from flask import Flask


app = Flask(__name__)

#cada ruta define una función
#y es lo que se ve de afuera como una pagina.
#si dos rutas van delante de una función,
#entonces ambas ejecutan la misma...
@app.route("/")
@app.route("/index")
def index():
    return "<h1>Bienvenidos!</h1>"
#testear flask:
#desde terminal ejecutar
# flask run 
# automaticamente buscará en el directorio de trabajo al archivo app.py

if __name__ == "__main__":
    #pass
    app.run(debug=True)