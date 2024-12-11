from sqlmodel import Field, SQLModel, create_engine, Session
from sqlalchemy import text

# Define el modelo
class instituciones(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    

# Crea la conexión a la base de datos

#engine = create_engine("sqlite:///./data/data.db")

engine = create_engine(
    "sqlite:///data.db",
    connect_args={"check_same_thread": False},  # Para permitir múltiples hilos en SQLite
    pool_size=10,  # Tamaño del pool (número de conexiones)
    max_overflow=20,  # Número máximo de conexiones adicionales que se pueden crear si el pool está lleno
    pool_timeout=30  # Tiempo de espera antes de que se agote el tiempo para obtener una conexión
                       
                       )


    # Conexión directa para ejecutar PRAGMAS
with engine.connect() as conn:
    conn.execute(text("PRAGMA journal_mode=WAL;"))
    conn.execute(text("PRAGMA synchronous=NORMAL;"))
    conn.execute(text("PRAGMA cache_size=10000;"))  # Puedes ajustar el número de páginas para caché
    conn.execute(text("PRAGMA temp_store = MEMORY;"))  # Almacena las tablas temporales en memoria
    conn.execute(text("PRAGMA locking_mode = NORMAL;"))  # Modo de bloqueo normal
    conn.execute(text("PRAGMA cache_spill = TRUE;"))



def get_session() -> Session:
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
