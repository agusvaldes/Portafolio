from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#el engine permite a SQLalchemy comunicarse con la base de datos

engine = create_engine("sqlite:///database/portafolio.db", connect_args={"check_same_thread":False} )
#ADVERTENCIA: crear el engine no conecta directamente con la base de datos

#Ahora creamos las sesion, lo que nos permite realizar operaciones dentro de nuesta BD
Session = sessionmaker(bind=engine)
session = Session()

#La siguiente instruccion se encarga de mapear la clase o clases creadas y vincularlas a la base de datos
Base = declarative_base()