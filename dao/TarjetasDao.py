from flask import current_app as app
from conexion.Conexion import Conexion

class TarjetasDao:
    def getTarjetas(self):
        tarjetasSQL="""
        select * from tarjetas
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tarjetasSQL)
            lista_tarjetas = cur.fetchall()
            lista_ordenada = []
            for item in lista_tarjetas:
                lista_ordenada.append({
                    "id": item[0],
                    "descripcion": item[1]
                    
                })
            print(lista_ordenada)
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close() 
        
    def guardarTarjetas(self,tarjetas):
        insertTarjetasSQL = """
        INSERT INTO tarjetas (descripcion) VALUES(%s)
        """
        conexion= Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(insertTarjetasSQL, (tarjetas,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)

        finally:
            cur.close()
            con.close()

            
        return False  
    
    def getTarjetasById(self, id):

        tarjetaSQL = """
        SELECT *
        FROM tarjetas WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tarjetaSQL, (id,))
            tarjetaEncontrada = cur.fetchone()
            return {
                    "id": tarjetaEncontrada[0],
                    "descripcion": tarjetaEncontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()
    
    def updateTarjetas(self, id, descripcion):

        tarjetaSQL = """
        UPDATE tarjetas
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(tarjetaSQL, (descripcion, id,))
            con.commit()

            return True

        except con.Error as e:
            app.logger.info(e)

        finally:
            cur.close()
            con.close()

        return False
    
    
    def deleteTarjetas(self, id):

        tarjetaSQL = """
        DELETE FROM tarjetas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(tarjetaSQL, (id,))
            con.commit()

            return True

        except con.Error as e:
            app.logger.info(e)

        finally:
            cur.close()
            con.close()

        return False