import sqlite3


class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria ")
            print("1- Cargar Automovil ")
            print("2- Modificar Automovil ")
            print("3- Borrar un Automovil ")
            print("4- Cargar disponibilidad ")
            print("5- Listado de Automoviles ")
            print("0- Salir de menu ")
            nro = int(input("Por favor ingrese un número "))
            if nro == 1:
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input(
                    "Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automovil(
                    marca, modelo, precio, cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
            if nro == 2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
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
            if nro == 0:
                break

    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute(
            "CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")
        conexion.miConexion.commit()
        conexion.cerrarConexion()


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
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(
                self.marca, self.modelo, self.precio, self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()

    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(
                self.precio, self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()

    def borrar_auto(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}' ".format(
                    self.marca, self.modelo))
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
            conexion.miCursor.execute(
                "UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles + 1 where marca='{}' and modelo='{}'".format(self.marca, self.modelo))
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
            print(autos)
            # for auto in autos:
            #id, marca, modelo, precio, cantidadDisponibles = auto

        except:
            print('Error al mostrar los autos')
        finally:
            conexion.cerrarConexion()


class Conexiones:

    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()


programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
