from tkinter import *

#Establecemos la página principal del programa

def inicio():

    global ventanaInicio
    ventanaInicio = Tk()
    ventanaInicio.title("Inicio")
    ventanaInicio.state('zoomed')
    
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

    Button(ventanaInicio, text = "Mostrar datos", height="3", width="30").pack()
    Label(ventanaInicio, text = "").pack()
    
    Button(ventanaInicio, text = "Actualizar datos", height="3", width="30").pack()
    Label(ventanaInicio, text = "").pack()
    
    Button(ventanaInicio, text="Eliminar datos", height="3", width="30").pack()
    
    

    #Label(ventanaInicio, text = "Ejemplo texto").pack()    
    #Button(ventanaInicio, text="Ventana Ejemplo", height="3", width="30", command = funcionVentanaEjemplo).pack()    



    ventanaInicio.mainloop()
    
if __name__ == "__main__":
    inicio()