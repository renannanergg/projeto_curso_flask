import os

SECRET_KEY = 'renan'

SQLALCHEMY_DATABASE_URI = \
            '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
                SGBD = 'mysql+mysqlconnector',
                usuario = 'root',
                senha = 'Acesan9900',
                servidor = 'localhost',
                database = 'jogoteca'
            )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'