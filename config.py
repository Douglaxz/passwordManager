#from flask_sqlalchemy import SQLAlchemy
import os

SECRET_KEY = 'passwordmanager111'


# conexão com o banco de dados mysql
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD ='mysql+mysqlconnector',
        usuario ='root',
        senha = '12345',
        servidor ='localhost',
        database ='db_passwordmanager')


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

ROWS_PER_PAGE = 10
