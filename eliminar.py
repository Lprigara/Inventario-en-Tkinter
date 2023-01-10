from tkinter import *
from sqlalchemy import delete



def eliminadoDatos(nombre):
    
    session = Session()
    session.query(Producto).filter(Producto.name == nombre).delete()
    session.commit()
    session.close()


def ventanaEliminar():
    global ventanaEliminado
    ventanaEliminado = Toplevel()
    ventanaEliminado.title("Eliminado")
    ventanaEliminado.state('zoomed')
    
    global imagen 
    imagen = PhotoImage(file="imagen.png")
    imagen = imagen.subsample(2,2)
    Label(ventanaEliminado, image = imagen).pack()
    Label(ventanaEliminado, text="Por favor el nombre del producto que desee eliminar:", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(ventanaEliminado, text="").pack()
    global nombre
    nombre = StringVar()
    global eliminadoNombre
    Label(ventanaEliminado, text="Introduzca el nombre del producto: ").pack()
    eliminadoNombre = Entry(ventanaEliminado, textvariable = nombre).pack()
    
    Label(ventanaEliminado, text= "").pack()
    Button(ventanaEliminado, text="Continuar",height="3", width="30" , command = lambda: eliminadoDatos(nombre.get()) ).pack()