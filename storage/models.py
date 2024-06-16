from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm.properties import ForeignKey
from database import Base


class Phonebook(Base):
    __tablename__ = "Phonebook"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    phonebook_id: Mapped[int]


class Contact(Base):
    __tablename__ = "Contact"
    id: Mapped[int] = mapped_column(primary_key=True)
    phonebook_id: Mapped[int] = mapped_column(ForeignKey("phonebook.phonebook_id"))
    first_name: Mapped[str]
    last_name: Mapped[str]
    number_telephone: Mapped[str]
    info: Mapped[str]

