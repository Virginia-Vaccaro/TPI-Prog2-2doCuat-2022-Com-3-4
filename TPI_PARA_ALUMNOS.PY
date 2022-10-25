from datetime import date
from multiprocessing.sharedctypes import Value
import sqlite3
from conexiones import Conexiones
from automoviles import Automovil
from motocicletas import Motocicleta


class ProgramaPrincipal:

    def menu(self):
        while True:
            try:
                print("Menu de opciones Concesionaria ")
                print("1- Cargar Automovil ")
                print("2- Modificar Automovil ")
                print("3- Borrar un Automovil ")
                print("4- Cargar disponibilidad ")
                print("5- Listado de Automoviles ")
                print("6- Cargar Motocicleta ")
                print("7- Modificar Precio Motocicleta(10%)")
                print("8- Mostrar registros de Motos anteriores a cierta fecha ")
                print("9- Listado de Motocicletas ")
                print("0- Salir de menu ")
                nro = int(input("Por favor ingrese un número "))
            except(ValueError, TypeError):
                print("Debe ingresar un número entero dentro de las opciones del menú.")
            else:
                if nro<0 or nro>9:
                    print("Debe ingresar un número entero dentro de las opciones del menú.")
                if nro == 1:
                    marca = input("Por favor ingrese la marca del automovil: ")
                    modelo = input("Por favor ingrese el modelo del automovil: ")
                    precio= programa.valida_precio()
                    cantidadDisponibles = programa.valida_disponibilidad()
                    nuevo_automovil = Automovil(marca, modelo, precio, cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                if nro == 2:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    precio= programa.valida_precio()
                    automovil_a_modificar = Automovil(marca, modelo, precio)
                    automovil_a_modificar.modificar_automoviles()
                if nro == 3:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    automovil_a_borrar = Automovil(marca, modelo)
                    automovil_a_borrar.borrar_auto()
                if nro == 4:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    automovil_a_modificar_disponibilidad = Automovil(marca, modelo)
                    automovil_a_modificar_disponibilidad.modificar_disponibilidad()
                if nro == 5:
                    Automovil.mostrar_autos()
                if nro == 6:
                    marca = input("Por favor ingrese la marca de la motocicleta: ")
                    modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                    precio= programa.valida_precio()
                    cilindrada = input("Por favor ingrese la cilindrada la motocicleta: ")
                    color = programa.valida_color()
                    fechaUltimoPrecio = date.today()
                    nueva_motocicleta = Motocicleta(marca,modelo,precio, cilindrada, color, fechaUltimoPrecio)
                    nueva_motocicleta.cargar_motocicletas()
                if nro == 7:
                    Motocicleta.pasar_historico()
                    Motocicleta.actualizar_precios()
                if nro == 8:
                    fecha = input("Por favor, ingrese una fecha en el siguiente formato (AAAA-MM-DD): ") 
                    Motocicleta.mostrar_anteriores(fecha)
                if nro == 9:
                    Motocicleta.mostrar_motocicletas()    
                if nro == 0:
                   print("Cerrando programa.")
                   break

            
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")
        conexion.miConexion.commit()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , marca  VARCHAR(30), modelo  VARCHAR(30), precio INTEGER NOT NULL, cilindrada  VARCHAR(30), color  VARCHAR(30), fechaUltimoPrecio DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)")   
        conexion.miConexion.commit()
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETAS (id_moto INTEGER , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio INTEGER, cilindrada VARCHAR(30), color VARCHAR(30), fechaUltimoPrecio DATETIME)")
        conexion.miConexion.commit()
        conexion.cerrarConexion()
 
    
    def valida_precio(self):
        while True:
            try:
                precio1 = float(input("Por favor ingrese el precio: "))
            except ValueError:
                print("Debe ingresar un valor numérico positivo.")
            else:
                if precio1<0:
                    print("Debe ingresar un número positivo.")
                if precio1>0:
                    return precio1
                    
                
    def valida_disponibilidad(self):
        while True:
            try:
                cantidadDisponibles1 = int(input("Por favor ingrese la cantidad de unidades disponibles: "))
            except ValueError:
                print("Debe ingresar un valor entero positivo.")
            else:
                if cantidadDisponibles1<0:
                    print("Debe ingresar un número positivo.")
                if cantidadDisponibles1 >0:
                    return cantidadDisponibles1

    
    def valida_color(self):
        while True:
            try:
                color = str(input("Por favor ingrese el color de la motocicleta: "))
            except TypeError:
                print("Debe ingresar un color. Vuelve a intentarlo.")
            else:
                if color.isalpha():
                    return color
                else:
                    print("Error, color inválido.")



programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
