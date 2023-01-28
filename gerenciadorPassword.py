# importação de dependencias
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import generate_password_hash, Bcrypt


# definição de chave
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
#csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)


from views import *

if __name__ == '__main__':
    app.run(debug=True)