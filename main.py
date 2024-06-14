import asyncio

from IO_file import read_file, save_file
from models import Person


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


if __name__ == "__main__":
    asyncio.run(main())
