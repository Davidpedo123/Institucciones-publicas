from config import get_session, instituciones
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

class Instituciones:
    nombres = None

    @classmethod
    async def cargar_datos(cls, session: AsyncSession = Depends(get_session)):
        if cls.nombres is None:
            # Ejecutar la consulta de manera asíncrona
            consulta = select(instituciones.nombre)
            resultados = await session.execute(consulta)  
            resultados = resultados.all()  
            cls.nombres = [{"nombre": institucion[0]} for institucion in resultados]  
        return cls.nombres
