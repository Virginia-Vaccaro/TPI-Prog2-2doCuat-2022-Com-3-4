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
            print("6- Cargar Motocicleta ")
            print("7- Modificar Precio Motocicleta(10%)")
            print("0- Salir de menu ")
            nro = int(input("Por favor ingrese un número "))
            if nro == 1:
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automovil(marca, modelo, precio, cantidadDisponibles)
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
            if nro == 6:
                marca = input("Por favor ingrese la marca de la motocicleta: ")
                modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                precio = input("Por favor ingrese el precio de la motocicleta: ")
                cilindrada = input("Por favor ingrese la cilindrada la motocicleta: ")
                color = input("Por favor ingrese el color de la motocicleta: ")
                nueva_motocicleta = Motocicleta(marca,modelo,precio, cilindrada, color)
                nueva_motocicleta.cargar_motocicletas()
            if nro == 7:
                Motocicleta.actualizar_precios()
            if nro == 0:
                break

    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")
        conexion.miConexion.commit()
        conexion.cerrarConexion()

    def crearTablasMotocicletas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , modelo  VARCHAR(30), marca  VARCHAR(30), cilindrada  VARCHAR(30), precio INTEGER NOT NULL, color  VARCHAR(30), cantidadDisponibles INTEGER NOT NULL, fechaUltimoPrecio DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)")   
        conexion.miConexion.commit()       
        conexion.cerrarConexion()
        
    def crearTablasMotoHis(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETAS (id_moto INTEGER , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio INTEGER, cilindrada VARCHAR(30), color VARCHAR(30), fechaUltimoPrecio DATETIME)")
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
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles + 1 where marca='{}' and modelo='{}'".format(self.marca, self.modelo))
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

class Motocicleta:
    def __init__(self, marca, modelo, precio, cilindrada, color):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cilindrada = cilindrada
        self.color = color

    
    def cargar_motocicletas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS (marca,modelo,precio,cilindrada,color) VALUES('{}','{}','{}','{}','{}')".format(self.marca,self.modelo,self.precio,self.cilindrada,self.color))
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
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio=(precio - ((precio*10)/100))")
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
                id, marca, modelo, precio, cilindrada, color = moto
                conexion.miCursor.execute("INSERT INTO HISTORICO_MOTOCICLETAS (id_moto, marca, modelo, precio, cilindrada, color, fechaUltimoPrecio) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(id,marca,modelo,precio,cilindrada,color))
                conexion.miConexion.commit()
        except:
            print("Ha ocurrido un error al pasar los historiales")
        finally:
            conexion.cerrarConexion      
class Conexiones:

    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()


programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
