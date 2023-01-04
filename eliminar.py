from tkinter import *
from main import ventanaInicio
from declarative_base import Session, engine, Base
from sqlalchemy import delete


class Eliminar():    

    def eliminadoDatos(self, nombre):
        
        session = Session()

        session.query(Producto).filter(Producto.name == nombre).delete()

        session.commit()

        session.close()
    

    
    def ventanaEliminar(self):

        global ventanaEliminado
        ventanaEliminado = Toplevel(ventanaInicio)
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



        Label(ventanaEliminado, text="nombre").pack()
        eliminadoNombre = Entry(ventanaEliminado, textvariable = nombre).pack()
        
        
        eliminadoNombre = Entry(ventanaEliminado, textvariable = nombre)
        eliminadoNombre.pack()
        
        

        Label(ventanaEliminado, text= "").pack()
        Button(ventanaEliminado, text="Continuar",height="3", width="30" , command = lambda: eliminadoDatos(nombre.get()) ).pack()

        
