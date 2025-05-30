import sqlite3
conexion = sqlite3.connect("Usuarios.db")
cursor = conexion.cursor()
cursor.execute("Select * from Usuarios")
for usuario in cursor.fetchall():
    print(f"Usuario: {usuario[0]}, Contraseña: {usuario[1]}")
conexion.close()