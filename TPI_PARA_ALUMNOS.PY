import sqlite3

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("2- Modificar Automovil")
            print("1- Cargar Automovil")
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número"))
            if nro == 1:
                marca = input("Por favor ingrese la marca del automovil: ")
                modelo = input("Por favor ingrese el modelo del automovil: ")
                precio = input("Por favor ingrese el precio del automovil: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
            if nro ==2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Automovil(marca,modelo,precio)
                automovil_a_modificar.modificar_automoviles()
            if nro==3:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                automovil_a_eliminar = Automovil(marca,modelo)
                automovil_a_eliminar.borrar_automovil()
            if nro==4:
                marca = input("Por favor ingrese el nombre de la marca: ")
                modelo = input("Por favor ingrese el nombre del modelo: ")
                automovil_disponibilidad = Automovil(marca,modelo)
                automovil_disponibilidad.cargar_disponibilidad()
            if nro==5:
                automovil_ordenado = Automovil()
                automovil_ordenado.listado_automoviles()
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
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
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automóvil modificado correctamente")
        except:
            print('Error al actualizar un automóvil')
        finally:
            conexion.cerrarConexion()


    def borrar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVIL where marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
            conexion.miConexion.commit
            print("Automóvil eliminado correctamente")
        except:
            print('Error al eliminar un automóvil')
        finally:
            conexion.cerrarConexion() 


    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:                                                     ###Completar####
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=          where marca='{}' and modelo='{}' ".format(self.cantidadDisponibles, self.marca,self.modelo))
            conexion.miConexion.commit
            print("Se ha actualizado la disponibilidad correctamente")
        except:
            print('Error al cargar la disponibilidad de un automovil')
        finally:
            conexion.cerrarConexion()


    def listado_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(" ") #########Completar##############
            conexion.miConexion.commit
            print("Lista ordenada de automóviles")
        except:
            print('Error al mostrar la lista de automóviles')
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