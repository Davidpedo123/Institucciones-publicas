from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from .config import get_session
from .dump import Instituciones

app = FastAPI()


@app.get("/api/instituciones")
async def get_instituciones(session: AsyncSession = Depends(get_session)):
    # Llamada asíncrona para cargar los datos
    nombres = await Instituciones.cargar_datos(session)
    
    return JSONResponse(
        content={"instituciones": nombres},
        media_type="application/json",
        headers={"Content-Length": "64868",
                 "Cache-Control": "max-age=604800"

                 
                 },
    )

