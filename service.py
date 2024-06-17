from routers import Person, Phonebook
from storage.storage import PhonebookStorage


class Service:
    async def get_file(self, filename: str, user_id: int):
        contacts = []
        async with open(file=filename, mode="r") as f:
            file_content = await f.read()
            for line in file_content.splitlines():
                if len(line) > 1:
                    person_data = [i.replace("\t", "") for i in line.split(", ")]
                    contacts.append(Person(
                        phonebook_id=1,
                        last_name=person_data[0],
                        first_name=person_data[1],
                        phone_number=person_data[2],
                        info=person_data[3]))
            for i in contacts:
                await PhonebookStorage.insert_contact(i)
            contacts.clear()

    async def get_list_phonebooks(self, user_id: int) -> list[Phonebook]:
        return await PhonebookStorage.get_phonebooks(user_id=user_id)

    async def get_contact_phonebook(self, user_id: int, phonebook_id: int) -> list[Person]:
        if PhonebookStorage.get_phonebooks(user_id=user_id) == phonebook_id:
            return await PhonebookStorage.get_contacts(
                phonebook_id=phonebook_id
            )
        else:
            return "Phonebook not found"

    async def get_contact_last_name(self, user_id: int, phonebook_id: int, last_name: str) -> list[Person]:
        if PhonebookStorage.get_phonebooks(user_id=user_id) == phonebook_id:
            return await PhonebookStorage.get_contacts_by_last_name(
                last_name=last_name,
                phonebook_id=phonebook_id
            )
        else:
            return "Phonebook not found"

    async def get_contact_phone_number(self, user_id: int, phonebook_id: int, phone_number: str) -> Person:
        if PhonebookStorage.get_phonebooks(user_id=user_id) == phonebook_id:
            return await PhonebookStorage.get_contacts_by_phome_number(
                phone_number=phone_number,
                phonebook_id=phonebook_id
            )
        else:
            return "Phonebook not found"