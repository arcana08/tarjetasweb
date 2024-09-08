import psycopg2

class Conexion:
    """metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=examenfinalbd user=postgres password=1")
    
    """getConexion
        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con