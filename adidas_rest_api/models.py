from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


DeclarativeBase = declarative_base()

def create_products_table(engine):
    DeclarativeBase.metadata.create_all(engine)
    
class Products(DeclarativeBase):
    __tablename__ = 'adidas_products'
    
    id = Column(Integer, primary_key = True)
    title = Column('title', String)
    brand = Column('brand', String)
    price = Column('price', String)
    store_keeping_unit = Column('store_keeping_unit', String)
    product_url = Column('product_url', String)

