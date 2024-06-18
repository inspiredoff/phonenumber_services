from routers import Phonebook, Person
from storage.storage import PhonebookStorage


# async def read_file(filename):
#     async with open(file=filename, mode="r") as f:
#         return await f.read()
#
# async def main():
#     content = await read_file("phon.txt")
#     for line in content.splitlines():
#         if len(line) > 1:
#             list_person = line.split(", ")
#             for i in range(len(list_person)):
#                 list_person[i] = list_person[i].replace("\t", "")
#             person = Person(list_person[0], list_person[1], list_person[2], list_person[3])
#             print(person.__str__())
#             await save_file("text.txt", person.__repr__())


class Service:
    async def get_file(filename: str, user_id):
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
                        info=person_data[3],
                    ))
            for contact in contacts:
                await PhonebookStorage.insert_contact(contact=contact)

    async def get_contact_phonebook(self, user_id: int, phonebook_id: int) -> list[Person] | str:
        if phonebook_id in PhonebookStorage.get_phonebooks(user_id=user_id):
            return await PhonebookStorage.get_contacts(
                phonebook_id=phonebook_id
            )
        else:
            return "Phonebook not found"

    async def get_list_phonebooks(self, user_id: int) -> list[Phonebook] | str:
        return await PhonebookStorage.get_phonebooks(user_id=user_id)

    async def get_contact_last_name(self, user_id: int, phonebook_id: int, last_name: str) -> Person | str:
        if phonebook_id in PhonebookStorage.get_phonebooks(user_id=user_id):
            return await PhonebookStorage.get_contacts_by_last_name(
                last_name=last_name,
                phonebook_id=phonebook_id
            )
        else:
            return "Phonebook not found"

    async def get_contact_phone_number(self, user_id: int, phonebook_id: int, phone_number: str) -> str:
        if phonebook_id in PhonebookStorage.get_phonebooks(user_id=user_id):
            return await PhonebookStorage.get_contacts_by_phome_number(
                phone_number=phone_number,
                phonebook_id=phonebook_id
            )
        else:
            return "Phonebook not found"

    async def get_contact_person_id(self, user_id: int, phonebook_id: int, person_id: int) -> Person | str:
        if phonebook_id in PhonebookStorage.get_phonebooks(user_id=user_id):
            return await PhonebookStorage.get_contacts_by_person_id(person_id=person_id)
        else:
            return "Phonebook not found"


phonebook_service = Service()
