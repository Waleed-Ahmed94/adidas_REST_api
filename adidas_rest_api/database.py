from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


user = 'postgres'
password = 'arbisoft'
host = 'localhost'
port = '5433'
database = 'adidas'

url = "postgres://{}:{}@{}:{}/{}".format(user,password,host,port,database)
engine = create_engine(url)

Session = sessionmaker(bind = engine)
session = scoped_session(Session)