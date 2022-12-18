# Mostrar productos
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3 as sql


# Función para mostrar productos
def showFunction():
    try:
        conexion = sql.connect("inventario.sqlite")
        cursor = conexion.cursor()
        print("La conexion a SQLite ha sido abierta")
        # Permitimos el cambio de todos los cambios menos de id para que sea unico e inmutable
        sql_query = '''SELECT * FROM producto'''
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        frm = Frame(ventanaShow)
        frm.pack(side=tk.TOP, padx=20, pady=40)
        tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="10")
        tv.pack()

        tv.heading(1, text="ID")
        tv.heading(2, text="Nombre")
        tv.heading(3, text="Cantidad")
        tv.heading(4, text="Precio")

        for i in rows:
            tv.insert('', 'end', values=i)

        conexion.commit()
        print("El registro del producto ha sido actualizado")
    except sql.Error as error:
        print("Error al mostrar la tabla:", error)
    else:
        cursor.close()
        conexion.close()
        print("La conexion a SQLite ha sido cerrada")

# Ventana para mostrar productos
global ventanaShow
ventanaShow = Tk()
ventanaShow.title("Mostrar Productos")
ventanaShow.state('zoomed')

# Mostramos la imagen
global image 
image = PhotoImage(file="imagen.png")
image = image.subsample(2,2)
Label(ventanaShow, image = image).pack()

# Ponemos el encabezado
Label(ventanaShow, text="Productos en el inventario", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()

# Ejecutamos la función
showFunction()

ventanaShow.mainloop()