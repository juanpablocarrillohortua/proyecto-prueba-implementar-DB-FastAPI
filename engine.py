from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

mysql_url = "mysql+aiomysql://root:@localhost:3306/heroes"
engine = create_async_engine(
    mysql_url, 
    echo=True,
    # MySQL a veces corta conexiones inactivas, esto ayuda a mantenerlas:
    pool_pre_ping=True 
)

async def get_session():
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session