import sqlite3
from sqlite3 import Error


class BD:
    def __init__(self, nombre_bd="basedatos.db"):
        self.nombre_bd = nombre_bd

    def conectar_bd(self):
        conexion = None
        try:
            conexion = sqlite3.connect(self.nombre_bd)
        except Error as e:
            print(f"Error al conectar la base de datos: {str(e)}")
        return conexion

    def crear_tabla(self):
        conexion = self.conectar_bd()
        cursor = conexion.cursor()
        try:
            sentencia = """CREATE TABLE IF NOT EXISTS producto (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            descripcion TEXT NOT NULL,
                            precio REAL NOT NULL)
                        """
            cursor.execute(sentencia)
            conexion.commit()
            print("Tabla de productos creada con éxito.")
        except Error as e:
            print(f"Error al crear la tabla: {str(e)}")
        finally:
            conexion.close()
