import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Table,Column,ForeignKey

# Obtener la contraseña de la base de datos de una variable de entorno
PASSWORD = os.getenv('DB_PASSWORD') 

# URL de la base de datos
URL_DB = f"mysql+pymysql://root:{PASSWORD}@127.0.0.1:3306/virtual_library"

# Crear el motor para la conexión
engine = create_engine(URL_DB, echo=True)

# Crear la clase base para los modelos
class Base(DeclarativeBase):
    pass

# Crear la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tabla de asociación entre usuarios y libros
users_books = Table(
    "users_book",
    Base.metadata,
    Column("user_id",ForeignKey("users.id"),primary_key=True),
    Column("book_id",ForeignKey("books.id"),primary_key=True)
)