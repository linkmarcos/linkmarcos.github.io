import sqlite3
nombre = input("Introduce tu nombre: ")
Contraseña = input("Introduce tu nueva Contraseña: ")
conexion = sqlite3.connect("Usuarios.db")
cursor = conexion.cursor()
cursor.execute("UPDATE Usuarios SET Contraseña = ? WHERE Nombre = ?", (Contraseña, nombre))
conexion.close()