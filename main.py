from tkinter import *
import sqlite3 as sql
import sys
import os
from producto import Producto
from declarative_base import Session, engine, Base

# Mostrar productos
def show():
    os.system('python show.py')
    
# Actualizar producto
def update():
    
    # Creamos la ventana
    global ventanaUpdate
    ventanaUpdate = Toplevel(ventanaInicio)
    ventanaUpdate.title("Actualizar datos")
    ventanaInicio.state('normal')
    
    # Mostramos la imagen
    Label(ventanaUpdate, image = image).pack()

    # Ponemos el encabezado
    Label(ventanaUpdate, text="Actualizar datos", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    
    # Mostramos un mensaje que indicara al usuario como actuar
    Label(ventanaUpdate, text="Por favor, introduzca los datos del producto a actualizar:", font=("Calibri", 15)).pack()
    Label(ventanaUpdate, text="").pack() 
    
    # Mostramos los campos a rellenar para actualizar el producto
    Label(ventanaUpdate, text= "ID del producto", font=("Calibri", 15)).pack()
    global id_prod
    id_prod = Entry(ventanaUpdate)
    id_prod.pack()
    Label(ventanaUpdate, text="").pack() 
    
    Label(ventanaUpdate, text= "Nombre del producto", font=("Calibri", 15)).pack()
    global name_prod
    name_prod = Entry(ventanaUpdate)
    name_prod.pack()
    Label(ventanaUpdate, text="").pack() 
    
    Label(ventanaUpdate, text= "Cantidad en stock", font=("Calibri", 15)).pack()
    global quantity_prod
    quantity_prod = Entry(ventanaUpdate)
    quantity_prod.pack()
    Label(ventanaUpdate, text="").pack() 
    
    Label(ventanaUpdate, text= "Precio del producto", font=("Calibri", 15)).pack()
    global price_prod
    price_prod = Entry(ventanaUpdate)
    price_prod.pack()
    Label(ventanaUpdate, text="").pack() 
    
    #Boton de Actualizar
    Button(ventanaUpdate, text = "Actualizar", height="3", width="30", command = updateFunction).pack()
    Label(ventanaUpdate, text="").pack()

def updateFunction():
    try:
        session = Session()
        producto1 = session.query(Producto).get(int(id_prod.get()))

        producto1.name = str(name_prod.get())
        producto1.quantity = int(quantity_prod.get())
        producto1.price = float(price_prod.get())
        if len(str(name_prod.get()).replace(" ", "")) != 0:
            session.add(producto1)
            session.commit()
            print("El registro del producto ha sido actualizado")
        else:
            raise Exception
    except Exception:
        print("Error al actualizar la tabla")
    else:
        session.close()
        print("La conexion con la base de datos ha sido cerrada")
    finally:
        id_prod.delete(0, END)
        name_prod.delete(0, END)
        quantity_prod.delete(0, END)
        price_prod.delete(0, END)  
  

#Establecemos la página principal del programa

def inicio():

    global ventanaInicio
    ventanaInicio = Tk()
    ventanaInicio.title("Inicio")
    ventanaInicio.state('normal')
    
    #Para añadir un icono de programa
    #ventanaInicio.iconbitmap("imagen2.ico")       

    global image 
    image = PhotoImage(file="imagen.png")
    image = image.subsample(2,2)
    Label(ventanaInicio, image = image).pack()

    Label(ventanaInicio, text="Acceso al sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(ventanaInicio, text="").pack()   

    Button(ventanaInicio, text = "Introducir datos", height="3", width="30").pack()
    Label(ventanaInicio, text = "").pack()

    Button(ventanaInicio, text = "Mostrar datos", height="3", width="30", command = show).pack()
    Label(ventanaInicio, text = "").pack()
    
    Button(ventanaInicio, text = "Actualizar datos", height="3", width="30", command = update).pack()
    Label(ventanaInicio, text = "").pack()
    
    Button(ventanaInicio, text="Eliminar datos", height="3", width="30").pack()
    
    

    #Label(ventanaInicio, text = "Ejemplo texto").pack()    
    #Button(ventanaInicio, text="Ventana Ejemplo", height="3", width="30", command = funcionVentanaEjemplo).pack()    



    ventanaInicio.mainloop()
    
if __name__ == "__main__":
    inicio()