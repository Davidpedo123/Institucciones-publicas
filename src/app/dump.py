from config import get_session, instituciones
from sqlmodel import select, Session
from fastapi import Depends

class Instituciones:
    nombres = None

    @classmethod
    def cargar_datos(cls, session: Session = Depends(get_session)):
        if cls.nombres is None:
            consulta = select(instituciones.nombre)
            resultados = session.exec(consulta).all()
            cls.nombres = [{"nombre": institucion} for institucion in resultados]
        return cls.nombres
