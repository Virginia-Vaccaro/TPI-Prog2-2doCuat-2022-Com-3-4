from datetime import date
from multiprocessing.sharedctypes import Value
import sqlite3
from conexiones import Conexiones

class Motocicleta:
    def __init__(self, marca, modelo, precio, cilindrada, color, fechaUltimoPrecio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cilindrada = cilindrada
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio

    
    def cargar_motocicletas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS (marca,modelo,precio,cilindrada,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}', '{}')".format(self.marca,self.modelo,self.precio,self.cilindrada,self.color,self.fechaUltimoPrecio))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
        except:
            print("Error al agregar la motocicleta")
        finally:
            conexion.cerrarConexion()
     
    @classmethod
    def actualizar_precios(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio= precio + (precio*0.1), fechaUltimoPrecio= CURRENT_TIMESTAMP")
            conexion.miConexion.commit()
            print("Motocicleta modificado correctamente")
        except:
            print('Error al actualizar una monoticleta')
        finally:
            conexion.cerrarConexion() 
    
    @classmethod
    def pasar_historico(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motos = conexion.miCursor.fetchall()
            for moto in motos:
                id, marca, modelo, precio, cilindrada, color, fechaUltimoPrecio = moto
                conexion.miCursor.execute("INSERT INTO HISTORICO_MOTOCICLETAS (id_moto, marca, modelo, precio, cilindrada, color, fechaUltimoPrecio) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(id,marca,modelo,precio,cilindrada,color,fechaUltimoPrecio))
                conexion.miConexion.commit()                
        except:
            print("Ha ocurrido un error al pasar los historiales")
        finally:
            conexion.cerrarConexion  

    @classmethod
    def mostrar_anteriores(cls, fecha):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS WHERE fechaUltimoPrecio<fecha")
            motos = conexion.miCursor.fetchall()
            for moto in motos: 
                print(f" ID: {moto[0]}\n Marca: {moto[1]}\n Modelo: {moto[2]}\n Precio: {moto[3]}\n Cilindrada: {moto[4]}\n Color: {moto[5]}\n ")
        except:
            print("No hay registros anteriores a la fecha ingresada.")
        finally:
            conexion.cerrarConexion
    
    @classmethod
    def mostrar_motocicletas(cls):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motos = conexion.miCursor.fetchall()
            for moto in motos:
                print(f" ID : {moto[0]}\n Marca : {moto[1]}\n Modelo : {moto[2]}\n Precio : {moto[3]}\n Cilindrada : {moto[4]}\n Color : {moto[5]}\n Fecha : {moto[6]}")
        except:
            print("Error al mostrar motocicletas")
        finally:
            conexion.cerrarConexion()