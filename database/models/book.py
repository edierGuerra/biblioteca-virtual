from database.db import Base,users_books
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer,String

class BookModel(Base):
    __tablename__ = "books"
    #Atributos
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    title:Mapped[str] = mapped_column(String(50),nullable=False,unique=True)
    autor:Mapped[str] = mapped_column(String(50),nullable=True)
    sipnopsis:Mapped[str] = mapped_column(String(250),nullable=True,unique=True)
    #Relaciones
    users:Mapped[list["UserModel"]] = relationship(
        secondary=users_books,
        back_populates="books"
        )
