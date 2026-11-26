import mysql.connector
from tkinter import messagebox
try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_coches'
    )
    cursor=conexion.cursor(buffered=True)

except:

    messagebox.showerror("Error de conexion", "No se pudo conectar a la Base de Datos, intentelo mas tarde")