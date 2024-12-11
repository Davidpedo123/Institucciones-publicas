from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from dump import Instituciones
from sqlmodel import Session
from config import instituciones, get_session
import json

app = FastAPI()


@app.get("/api/instituciones")
async def get_instituciones(session: Session = Depends(get_session)):
    
    
    nombres = Instituciones.cargar_datos(session)
    
    return JSONResponse(
        content={"instituciones": nombres},
        media_type="application/json",
        headers={"Content-Length": "64868",
                 "Cache-Control": "max-age=604800"

                 
                 },
    )

