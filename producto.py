from sqlalchemy import Column, Integer, String, Float
from declarative_base import Base

class Producto(Base):

  __tablename__ = 'producto'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  quantity = Column(Integer)
  price = Column(Float)