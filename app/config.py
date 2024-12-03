from sqlmodel import Field, SQLModel, create_engine, Session

# Define el modelo
class Institucion(SQLModel, table=True):
    nombre: str
    ubicacion: str

# Crea la conexión a la base de datos
engine = create_engine("sqlite:///./instituciones.db")
