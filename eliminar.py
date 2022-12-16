from producto import Producto
from declarative_base import Session, engine, Base

if __name__ == '__main__':
    #Crea la BD
    Base.metadata.create_all(engine)

    #Abre la sesión
    session = Session()

    #crear producto
    producto1 = Producto(name = "Raqueta", quantity = 5, price = 19.99)
    producto2 = Producto(name = "Pelota tenis", quantity = 10, price = 1.99)
    producto3 = Producto(name = "Calcetines Nike", quantity = 7, price = 8.99)
    producto4 = Producto(name = "Visera Nike", quantity = 5, price = 13.99)

    #Insertar productos en BBDD
    session.add(producto1)
    session.add(producto2)
    session.add(producto3)
    session.add(producto4)

    #Commit
    session.commit()

    #Close
    session.close()