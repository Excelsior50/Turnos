#Conexion db

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin123@localhost/turnos_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
