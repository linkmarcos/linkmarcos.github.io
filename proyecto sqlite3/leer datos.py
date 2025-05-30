import sqlite3
nombre = input("Introduce tu nombre: ")
Contraseña = input("Introduce tu Contraseña: ")
conexion = sqlite3.connect("Usuarios.db")
cursor = conexion.cursor()
cursor.execute("Select * from Usuarios where Nombre = ? and Contraseña = ?", (nombre, Contraseña))
for usuario in cursor.fetchall():
    print(f"Usuario: {usuario[0]}, Contraseña: {usuario[1]}")
conexion.close()