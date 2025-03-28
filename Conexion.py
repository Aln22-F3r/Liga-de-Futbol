import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kanibal1",
            database="liga_futbol",
            port=3308
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
        return conexion
    except mysql.connector.Error as error:
        print(f"No se pudo establecer la conexión: {error}")
        return None

# Llamada a la función para probar la conexión
conectar()