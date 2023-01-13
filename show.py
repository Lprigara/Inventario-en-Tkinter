# Mostrar productos
import tkinter as tk
from tkinter import *
from tkinter import ttk
from declarative_base import Session, engine, Base
from producto import Producto

# Función para mostrar productos
def showFunction():

    #Abre la sesión
    session = Session()
    print("La conexion a SQLite ha sido abierta")
    
    frm = Frame(ventanaShow)
    frm.pack(side=tk.TOP, padx=20, pady=40)
    tv = ttk.Treeview(frm, selectmode='browse')
    tv.grid(row=1, column=1, padx=20, pady=20)
    
    # Number of Columns
    tv["columns"] = ('1', '2', '3', '4')

    # Defining heading
    tv["show"] = 'headings'

    # Width of columns and aligment
    tv.column('1', width=30, anchor='c')
    tv.column('2', width=200, anchor='c')
    tv.column('3', width=120, anchor='c')
    tv.column('4', width=120, anchor='c')

    # Headngs respective columns
    tv.heading('1', text="ID")
    tv.heading('2', text="Nombre")
    tv.heading('3', text="Cantidad")
    tv.heading('4', text="Precio")

    #Hace la query
    productos = session.query(Producto).all()

    #Printing
    for producto in productos:
        tv.insert('', 'end', iid=producto.id, values=(producto.id, producto.name, producto.quantity, producto.price))
    print("Los productos han sido mostrados")

    #Close
    session.close()
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
