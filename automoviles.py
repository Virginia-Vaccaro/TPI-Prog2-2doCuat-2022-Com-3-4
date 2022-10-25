from datetime import date
from multiprocessing.sharedctypes import Value
import sqlite3
from conexiones import Conexiones


class Automovil:
    def __init__(self, marca, modelo, precio=None, cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cantidadDisponibles = cantidadDisponibles

    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo, self.precio, self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automóvil cargado exitosamente")
        except:
            print("Error al agregar un automóvil")
        finally:
            conexion.cerrarConexion()

    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio, self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Automóvil modificado correctamente")
        except:
            print('Error al actualizar un automóvil')
        finally:
            conexion.cerrarConexion()

    def borrar_auto(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}' ".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Automovil eliminado correctamente")
        except:
            print('Error al borrar un automovil')
        finally:
            conexion.cerrarConexion()

    def modificar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles= cantidadDisponibles + 1 where marca='{}' and modelo='{}'".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Cantidad disponible del auto modificada correctamente")
        except:
            print('Error al actualizar la cantidad disponible')
        finally:
            conexion.cerrarConexion()

    @classmethod
    def mostrar_autos(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos = conexion.miCursor.fetchall()
            # print(autos)
            for auto in autos:
                print(f" ID : {auto[0]}\n Marca : {auto[1]}\n Modelo : {auto[2]}\n Precio : {auto[3]}\n Disponibles : {auto[4]}")
        except:
            print("Error al mostrar automoviles")
        finally:
            conexion.cerrarConexion()