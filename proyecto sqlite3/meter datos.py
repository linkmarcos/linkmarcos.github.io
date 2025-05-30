import sqlite3
nombre = input("Introduce tu nombre: ")
Contraseña = input("Introduce tu Contraseña: ")
conexion = sqlite3.connect("Usuarios.db")
cursor = conexion.cursor()
cursor.execute("Insert into Usuarios (Nombre, Contraseña) values (?, ?)", (nombre, Contraseña))
conexion.commit()
cursor.execute("Select * from Usuarios")
for fila in cursor.fetchall():
    print(fila)