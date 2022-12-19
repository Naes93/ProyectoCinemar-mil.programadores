import sqlite3
from datetime import date
import hashlib

database = "cine.sql" # todo: por ahora ponemos el nombre de la base aqui, ver mejor opcion

class Db:
    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()            
    
    @staticmethod
    def consultar(consulta, pametros = (), fetchAll = True):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, pametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear_tablas():
        sql_usuarios = '''CREATE TABLE IF NOT EXISTS "Usuarios" (
                                "UsuarioId"	INTEGER NOT NULL,
                                "Apellido"	VARCHAR(25),
                                "Nombre"	VARCHAR(30),
                                "FechaNacimiento"	VARCHAR(8),
                                "Dni"	INTEGER,
                                "CorreoElectronico"	VARCHAR(25),
                                "Usuario"	VARCHAR(15) UNIQUE,
                                "Contrasenia"	VARCHAR(10),
                                "RolId"	INTEGER,
                                "Activo"	INTEGER NOT NULL DEFAULT 1,
                                PRIMARY KEY("UsuarioId" AUTOINCREMENT)
                            );'''
        sql_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                            "RolId"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(15) NOT NULL UNIQUE,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("RolId")
                        );'''
         sql_administracion = ''' CREATE TABLE IF NOT EXISTS "Administracion" (
	"CantReservas"	VARCHAR(25),
	"IdUsuario" INTEGER,
	"IdReserva"	INTEGER NOT NULL,
	"IdPelicula" INTEGER,
	"Id_Sala" INTEGER,
	"Idfuncion"	TEXT NOT NULL,
	"IdDescuento"	NUMERIC NOT NULL,
	"Id_Estreno"	BLOB NOT NULL)
            );'''
                        
        sql_pelicula = ''' CREATE TABLE IF NOT EXISTS "Peliculas" (
      "IDPelicula"	INTEGER,
     	"Nombre_pelicula" VARCHAR (15) NOT NULL,
	    "Categorias" VARCHAR (25) NOT NULL,
	    "Tipo_Pelis"	INTEGER NOT NULL,
    	"Sala"	INTEGER,
    	"IdFormato" INTEGER,
	    "Hs_funcion" VARCHAR(5),
    	"Activo" INTEGER NOT NULL DEFAULT,
	    FOREIGN KEY ("Sala") REFERENCES "Peliculas"("Sala"),
      	PRIMARY KEY("IDPelis")
            ):'''
            
          sql_funcion = '''CREATE TABLE IF NOT EXISTS "Funcion" (
               "Idfuncion" INTEGER,
               "horario" VARCHAR(6),
               "dia" VARCHAR(8),
               "Id_Sala" INTEGER,
               FOREIGN KEY("Id_Sala") REFERENCES sala("Id_Sala")
               PRIMARY KEY ("Idfuncion")
               );'''
                        
         sql_reserva = '''CREATE TABLE IF NOT EXISTS "Reserva" (
	"IdReserva"	INTEGER,
	"FechaReserva"	VARCHAR(8),
	"precio_entrada" INTEGER,
	"IdDescuento"	INTEGER,
	"IdPelicula"	INTEGER,
	"IdUsuario"	INTEGER,
	PRIMARY KEY("IdReserva"),
	FOREIGN KEY ("IdDescuento") REFERENCES Descuento ("IdDescuento")
	FOREIGN KEY ("IdPelicula") REFERENCES Peliculas ("IdPelicula")
	FOREIGN KEY("IdUsuario") REFERENCES "Reserva"("IdUsuario")
);'''
                        
          sql_salas = ''' CREATE TABLE IF NOT EXISTS "Salas" (
	"Id_Sala"	INTEGER NOT NULL,
	"NombreSala"	TEXT NOT NULL UNIQUE,
	"Tipo" TEXT NOT NULL,
	"Capacidad"	INTEGER NOT NULL,
	"Activo" INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY("Id_Sala" AUTOINCREMENT)
          );'''
                        
          sql_butaca = ''' CREATE TABLE IF NOT EXISTS "Butaca" ON "Administracion" (
          "Id_asiento" INTEGER,
          "ocupado" BOOL,
          "Idfuncion" INTEGER,
          "IdReserva" INTEGER,
          FOREIGN KEY(Idfuncion) REFERENCES funcion(Idfuncion),
          FOREIGN KEY(IdReserva) REFERENCES Reserva (IdReserva)
          PRIMARY KEY ("Id_asiento" INTEGER)
            );'''
                        
          sql_descuento = ''' CREATE TABLE IF NOT EXISTS "Descuento" (
	"IdDescuento"	VARCHAR,
	"DiaDescuento"	VARCHAR,
	"PorcentajeDescuento"	INTEGER,
	"IdReserva" INTEGER,
	FOREIGN KEY (IdReserva) REFERENCES Reserva (IdReserva)
	PRIMARY KEY("IdDescuento")
            );'''
                      
        tablas = {"Usuarios": sql_usuarios, "Roles": sql_roles,"Administracion": sql_administracion, "Peliculas": sql_pelicula,"Funcion": sql_funcion ,"Reserva": sql_reserva,"Salas": sql_salas, "Butaca": sql_butaca, "Descuento": sql_descuento }

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
                # TODO agregar commit
            
    @staticmethod
    def poblar_tablas():        
       
        sql_roles = '''INSERT INTO Roles (RolId, Nombre) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente"),
                        ;'''
                        
                        
        sql_pelicula ='''INSERT INTO Salas (NombreSala, Tipo, Capacidad )
                    VALUES
                        ("1", "2D", "50"),
                        ("2","3D", "60")
                        :'''
                        
       sql_funcion ='''INSERT INTO Salas (NombreSala, Tipo, Capacidad )
                    VALUES
                        ("1", "2D", "50"),
                        ("2","3D", "60")
                        :'''
                        
        sql_reserva ='''INSERT INTO Salas (NombreSala, Tipo, Capacidad )
                    VALUES
                        ("1", "2D", "50"),
                        ("2","3D", "60")
                        :'''
        
        
        sql_salas ='''INSERT INTO Salas (NombreSala, Tipo, Capacidad )
                    VALUES
                        ("1", "2D", "50"),
                        ("2","3D", "60")
                        :'''
                       
         sql_butaca ='''INSERT INTO Butaca (Id_asiento, ocupado, Idfuncion,IdReserva)
                    VALUES
                        ("1", "2D", "50"),
                        ("2","3D", "60")
                        :''' 
                        
         sql_descuento ='''INSERT INTO Descuento (IdDescuento, DiaDescuento, PorcentajeDescuento)
                    VALUES
                      ("001", "Lunes", "20"),
                      ("002","Martes", "15"),
                     ("003","Miercoles","20"),
                      ("004", "Jueves", "15"),
                      ("005","Viernes", "10"),
                      ("006","Sabado", "10"),
                      ("007","Domingo", "10"),
                        :'''
          
        tablas = { "Roles": sql_roles, "Salas": sql_salas }

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()
        
        