import asyncio
from src.storage.storage import PhonebookStorage

asyncio.run(PhonebookStorage.create_table())