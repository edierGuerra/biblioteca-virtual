from database.db import Base,users_books
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer,String

class UserModel(Base):
    __tablename__ = "users"
    #Atributos
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(150),nullable=False)
    email:Mapped[str] = mapped_column(String(150),nullable=False)
    password:Mapped[str] = mapped_column(String(200),nullable=False)
    #Relaciones
    books:Mapped[list["BookModel"]] = relationship(
        secondary=users_books,
        back_populates="users"
        )
