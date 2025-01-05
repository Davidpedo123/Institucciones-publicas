from .config import get_session, instituciones
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

class Instituciones:
    nombres = None

    @classmethod
    async def cargar_datos(cls, session: AsyncSession = Depends(get_session)):
        if cls.nombres is None:
            # Ejecutar la consulta de manera asíncrona
            consulta = select(instituciones)
            resultados = await session.execute(consulta)
            
            # Convertir los resultados en una lista de diccionarios
            cls.nombres = [
                {
                    
                    "nombre": institucion.nombre,
                    "sigla": institucion.sigla,
                    "ubicacion": institucion.ubicacion,
                }
                for institucion in resultados.scalars().all()
            ]
        
        return cls.nombres

