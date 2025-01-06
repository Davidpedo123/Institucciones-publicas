from sqlmodel import Field, SQLModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class instituciones(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    sigla: str
    ubicacion: str
    lat_min : float
    lat_max : float
    lon_min : float
    lon_max : float

engine = create_async_engine(
    "sqlite+aiosqlite:///./data/data2.sqlite",  # Uso de aiosqlite como base de datos
    connect_args={"check_same_thread": False},  # Para SQLite en un solo hilo
)


async def init_db():
    async with engine.connect() as conn:
        
        await conn.execute(text("PRAGMA journal_mode=WAL;"))
        await conn.execute(text("PRAGMA synchronous=NORMAL;"))
        await conn.execute(text("PRAGMA cache_size=10000;"))
        await conn.execute(text("PRAGMA temp_store = MEMORY;"))
        await conn.execute(text("PRAGMA locking_mode = NORMAL;"))
        await conn.execute(text("PRAGMA cache_spill = TRUE;"))


async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session  
