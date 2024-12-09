from sqlmodel import Field, SQLModel, create_engine, Session

# Define el modelo
class instituciones(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    

# Crea la conexión a la base de datos
engine = create_engine("sqlite:///./data/data.db")

session = Session(engine)
