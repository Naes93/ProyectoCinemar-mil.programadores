import sqlite3
from datetime import date
import hashlib

database = "super.db" # todo: por ahora ponemos el nombre de la base aqui, ver mejor opcion

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
            print(consulta)
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
                                "Apellido"	VARCHAR(50),
                                "Nombre"	VARCHAR(30),
                                "FechaNacimiento"	VARCHAR(23),
                                "Dni"	INTEGER,
                                "CorreoElectronico"	VARCHAR(30),
                                "Usuario"	VARCHAR(15) UNIQUE,
                                "Contrasenia"	VARCHAR(100),
                                "RolId"	INTEGER,
                                "Activo"	INTEGER NOT NULL DEFAULT 1,
                                PRIMARY KEY("UsuarioId" AUTOINCREMENT)
                            );'''
        sql_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                            "RolId"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(30) NOT NULL UNIQUE,
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
                
        sql_peliculas = '''CREATE TABLE IF NOT EXISTS "Peliculas" (
	                        "IdPelicula"	INTEGER,
                        	"Nombre_pelicula"	VARCHAR(50) NOT NULL,
	                        "Categorias"	VARCHAR(50) NOT NULL,
                        	"Sala"	INTEGER,
	                        "Hs_funcion"	INTEGER,
                        	"Activo"	INTEGER NOT NULL DEFAULT 1,
                        	FOREIGN KEY("Sala") REFERENCES "Peliculas"("Sala"),
                        	PRIMARY KEY("IdPelicula" AUTOINCREMENT)
                        );'''

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
                      

        tablas = {"Usuarios": sql_usuarios, "Roles": sql_roles, "Peliculas" : sql_peliculas,}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
                cnn.commit()
                # TODO agregar commit
            
    @staticmethod
    def poblar_tablas():        
        sql_roles = '''INSERT INTO Roles (RolId, Nombre) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente");'''
    
        tablas = {"Roles": sql_roles, "Pelicula": sql_pelicula }

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)

        sql_peliculas = '''INSERT INTO Peliculas (IdPelicula, Nombre_pelicula, Categorias, Sala, Hs_funcion) 
                    VALUES 
                        (1, "El Conjuro", "Terror", 2, "15:30"),
                        (2, "Avatar", "Cienciaficcion", 3, "19:00");'''
                        

        tablas = {"Peliculas": sql_peliculas}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql) 
                    cnn.commit()      

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
          tablas = {"Descuento": sql_descuento}
          with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql) 
                    cnn.commit()

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()
