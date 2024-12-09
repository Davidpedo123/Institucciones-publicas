from config import instituciones, session
from sqlmodel import select
from fastapi import FastAPI, Request

app = FastAPI()

consulta = select(instituciones.nombre)
resultados = session.exec(consulta).all()

nombres = [{"nombre": institucion} for institucion in resultados]


@app.get("/api/instituciones")
async def inst(request: Request):
    institucion = nombres
    return {"instituciones" : institucion}


import uvicorn

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8080)
