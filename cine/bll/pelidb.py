from dal.db import Db

def agregar(nombre, categoria, sala, hsfuncion):    
    sql = "INSERT INTO Peliculas(Nombre_pelicula, Categorias, Sala, Hs_funcion) VALUES(?, ?, ?, ?);"
    parametros = (nombre, categoria, sala, hsfuncion)
    Db.ejecutar(sql, parametros)

def actualizar(nombre, categoria, sala, hsfuncion, idpelic):    
    sql = "UPDATE Peliculas SET Nombre_pelicula = ?, Categorias = ?, Sala = ?, Hs_funcion = ? WHERE IdPelis = ? AND Activo = 1;"
    parametros = (nombre, categoria, sala, hsfuncion, idpelic)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE Peliculas SET Activo = 0 WHERE IdPelis = ? AND Activo = 1;"
    else:
        sql = "DELETE FROM Peliculas WHERE IdPelis = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT p.IdPelis, p.Nombre_pelicula, p.Categorias, p.Sala, p.Hs_funcion, p.Activo
            FROM Peliculas p
            WHERE p.Activo = 1;'''
    result = Db.consultar(sql)
    return result

def existe(pelicula):
    sql = "SELECT COUNT(*) FROM Peliculas WHERE Nombre_pelicula = ? AND Activo = 1;"
    parametros = (pelicula,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def obtener_id(id):
    sql = " SELECT * FROM peliculas WHERE IdPelis=?"
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)   
    print(result) 
    return result
    








