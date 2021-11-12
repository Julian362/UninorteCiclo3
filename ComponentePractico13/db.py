import sqlite3

from sqlite3 import Error

def conectar():
    try:
        conn = sqlite3.connect('DataBase/data.db')
        return conn
    except Error as err:
        print(err)
        return None

def ejecutar_insert(_sql,lista_parametros):
    try:
        conn = conectar()
        if conn:
            objeto_cursor = conn.cursor()
            filas = objeto_cursor.execute(_sql,lista_parametros).rowcount
            objeto_cursor.close()
            conn.commit()
            conn.close
            return filas
        else:
            print("No se pudo establecer la conexión a la base de datos. ver errores previos")
            return -1
    except Error as err:
        print("Error al ejecutar Sentenica SQL:"+str(err))
        return -1

def ejecutar_select(_sql,lista_parametros):
    try:
        conn = conectar()
        if conn:
            conn.row_factory = fabrica_diccionarios
            objeto_cursor = conn.cursor()

            if lista_parametros:
                objeto_cursor.execute(_sql, lista_parametros)
            else:
                objeto_cursor.execute(_sql)

            filas = objeto_cursor.fetchall()
            objeto_cursor.close
            conn.close
            return filas
        else:
            print("No se pudo establecer la conexión a la base de datos. ver errores previos")
            return None
    except Error as err:
        print("Error al ejecutar Sentenica SELECT SQL:"+str(err))
        return None

def fabrica_diccionarios(cursor, row):
    d={}
    for idx, col in enumerate(cursor.description):
        d[col[0]]=row[idx]

    return d