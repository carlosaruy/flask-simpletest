from flask import Flask
#para no cargar todo el html en el codigo python
#se utiliza el render_template.
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"]="UNA_PASSWORD_SUPERSEGURA_EN_GITHUB"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 

db = SQLAlchemy(app)


from routes import * 

if __name__ == "__main__":
    #pass
    app.run(debug=True)