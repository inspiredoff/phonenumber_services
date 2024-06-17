from routers import Phonebook, Person 

async def read_file(filename):
    async with open(file=filename, mode="r") as f:
        return await f.read()

async def main():
    content = await read_file("phon.txt")
    for line in content.splitlines():
        if len(line) > 1:
            list_person = line.split(", ")
            for i in range(len(list_person)):
                list_person[i] = list_person[i].replace("\t", "")
            person = Person(list_person[0], list_person[1], list_person[2], list_person[3])
            print(person.__str__())
            await save_file("text.txt", person.__repr__())


    class Service:
        async def get_file(filename:str, user_id):
            contacts = []
            async with open(file=filename, mode="r") as f:
                file_content = await f.read()
                for line in content.splitlines():
                    if len(line)>1:
                        person_data = [i.replace("\t","") for i in line.split(", ")]
                            contacts.append(Person(
                                phonebook_id=1,
                                last_name=person_data[0],
                                first_name=person_data[1],
                                phone_number=person_data[2],
                                info=person_data[3],
                                ))
