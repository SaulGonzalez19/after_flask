import sqlite3
from sqlite3 import Error
from turtle import end_fill
from config_db import BD

bd = BD()

class Producto():

    def select(self):
        conexion = bd.conectar_bd()
        conexion.row_factory = sqlite3.Row
        sentencia_sql = "SELECT * FROM producto"
        
        try:
            cursor = conexion.cursor()
            cursor.execute(sentencia_sql)
            dato_producto = cursor.fetchall()
            productos = [ dict(fila) for fila in dato_producto ]
            return productos
        except Error as e:
            print (f"Error con la instrucción: {str(e)}.")
        finally:
            conexion.close()

def select_by_id(self, id):
    conexion = bd.conectar_bd()
    sentencia_sql = f"SELECT * FROM producto WHERE id = {id}"
    conexion.row_factory = sqlite3.Row

    try:
            cursor = conexion.cursor()
            cursor.execute(sentencia_sql)
            datos_producto = dict(cursor.fetchone())
            return datos_producto
    except Error as e:
            print (f"Error con la instrucción: {str(e)}.")
    finally:
            conexion.close()

def insert(self, producto):
    conexion = bd.conectar_bd()
    sentencia_sql = "INSERT INTO producto (descripcion, precio) VALUES (?, ?)"
    parametros = (producto["descripcion"], producto["precio"])
    try:
        cursor = conexion.cursor()
        cursor.execute(sentencia_sql, parametros)
        conexion.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error al agregar el elemento: {str(e)}.")
        return False
    finally:
        conexion.close()

def update(self, id, producto):
    conexion = bd.conectar_bd()
    sentencia_sql = "UPDATE producto SET descripcion = ?, precio = ? WHERE id = ?"
    parametros = (producto["descripcion"], producto["precio"], id)
    try:
        cursor = conexion.cursor()
        cursor.execute(sentencia_sql, parametros)
        conexion.commit()
        producto_actualizado = self.select_by_id(id)
        return producto_actualizado
    except Error as e:
        print(f"Error con la actualización: {str(e)}")

    finally:
        conexion.close()

def delete(self, id):
    conexion = bd.conectar_bd()
    sentencia_sql = f"DELETE FROM producto WHERE id = {id}"
    mensaje = {}
    try:
        cursor = conexion.cursor()
        cursor.execute(sentencia_sql)
        conexion.commit()
        mensaje["status"] = "Producto eliminado con éxito"
        return mensaje
    except Error as e:
        print(f"No se ha podido eliminar el producto: {str(e)}")
    finally:
        conexion.close