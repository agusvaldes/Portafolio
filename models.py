from sqlalchemy import Column, Integer, String
import db

class Portafolio(db.Base):
    __tablename__= "contactos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    email = Column(String(200))
    mensaje = Column(String(200))
    asunto = Column(String(200))

    def __init__(self, nombre, email, mensaje,asunto):
        self.nombre = nombre
        self.email = email
        self.mensaje = mensaje
        self.asunto = asunto

        def __str__(self):
            return "Clientes({}: {}, {} {} {})".format(self.id, self.nombre, self.email, self.mensaje, self.asunto)