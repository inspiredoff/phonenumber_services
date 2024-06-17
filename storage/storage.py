from database import async_session_factory
from sqlalchemy.ext.asyncio import async_session
from sqlalchemy import select
from models import Phonebook, Contact
from routers import Person
import asyncpg


class PhonebookStorage:
    @staticmethod
    async def get_contacts(async_session: async_session_factory, phonebook_id: int):
        async with async_session() as session:
            quere = select(Contact).where(Contact.phonebook_id == phonebook_id)
            return await session.execute(quere).scalars().all()

    @staticmethod
    async def get_phonebooks(async_session: async_session_factory, user_id: int):
        async with async_session() as session:
            quere = select(Phonebook).where(Phonebook.user_id == user_id)
            return await session.execute(quere).scalars().all()

    @staticmethod
    async def insert_contact(async_session: async_session_factory, contact: [Person] or Person):
        if type(contact) == type(Person):
            data = Contact(
                phonebook_id=contact.phonebook_id,
                first_name=contact.first_name,
                last_name=contact.last_name,
                number_telephone=contact.phone_number,
                info=contact.info)
            async with async_session() as session:
                session.add(data)
            await session.commit()
        else:
            for i in contact:
                data = Contact(
                    phonebook_id=i.phonebook_id,
                    first_name=i.first_name,
                    last_name=i.last_name,
                    number_telephone=i.phone_number,
                    info=i.info)
                async with async_session() as session:
                    session.add(data)
            await session.commit()

    @staticmethod
    async def get_contacts_by_last_name(async_session: async_session_factory, last_name: str, phonebook_id: int):
        async with async_session() as session:
            quere = select(Contact).where(Contact.last_name == last_name and Contact.phonebook_id == phonebook_id)
            return await session.execute(quere).scalars().all()

    @staticmethod
    async def get_contacts_by_phome_number(async_session: async_session_factory, phone_number: str, phonebook_id: int):
        async with async_session() as session:
            quere = select(Contact).where(Contact.last_name == phone_number and Contact.phonebook_id == phonebook_id)
            return await session.execute(quere).scalars().all()
