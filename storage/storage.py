from database import async_session_factory
from sqlalchemy.ext.asyncio import async_session
from sqlalchemy import select
from models import Phonebook, Contact
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
    async def insert_contact(async_session: async_session_factory, contact: Contact):
        async with async_session() as session:
            session.add(contact)
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