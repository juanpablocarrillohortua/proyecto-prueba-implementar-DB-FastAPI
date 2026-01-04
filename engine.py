from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import ssl

#mysql_url = "mysql+aiomysql://root:@localhost:3306/heroes"

from urllib.parse import quote_plus # Agrega esta importación

# Define tus datos por separado para mayor claridad
user = "avnadmin"
password = "AVNS_4DnrTc5CAnZUBjJXJtT" # La que copias de Aiven
host = "heroesprueba-juanpablocarrillohortua-03b0.c.aivencloud.com"
port = "12007"
database = "heroes" # OJO: Verifica si en Aiven se llama 'heroes' o 'defaultdb'

# Codificamos la contraseña para que los caracteres especiales no rompan la URL
safe_password = quote_plus(password)

mysql_url = f"mysql+aiomysql://{user}:{safe_password}@{host}:{port}/{database}"
# Creamos un contexto SSL por defecto que sea seguro
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE # Aiven usa certificados autofirmados a veces


engine = create_async_engine(
    mysql_url,
    connect_args={"ssl": ssl_context} if "aivencloud" in mysql_url else {},
    pool_recycle=3600,
)

async def get_session():
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session