from pydantic import BaseModel
from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse

from IO_file import save_file, read_file

phonebook_router_v1 = APIRouter(prefix="/phonebook")


class Person(BaseModel):
    phonebook_id: int
    last_name: str
    first_name: str
    phone_number: str
    info: str


class Phonebook(BaseModel):
    user_id: int
    phonebook_id: int
    contacts: list[Person]


@phonebook_router_v1.post("/api/v1/upload-phonebook")
async def upload_phonebook(file: UploadFile):
    return read_file(file.filename)


@phonebook_router_v1.get("/api/v1/{user_id}/{phonebook_id}/contacts")
async def get_phonebook(user_id, phonebook_id):
    return Phonebook(user_id=user_id, phonebook_id=phonebook_id, contacts=[])


@phonebook_router_v1.get("/api/v1/{user_id}/{phonebook_id}/contacts/{person_id}")
async def get_contact_person_id():
    pass
    return


@phonebook_router_v1.get("/api/v1/{user_id}/{phonebook_id}/contacts/{last_name}")
async def get_contact_last_name():
    pass
    return


@phonebook_router_v1.get("/api/v1/{user_id}/{phonebook_id}/contacts/{phone_number}")
async def get_contact_phone_number():
    pass
    return


@phonebook_router_v1.post("/api/v1/{user_id}/{phonebook_id}/contacts")
async def post():
    pass
    return


@phonebook_router_v1.get("/api/v1/{user_id}/{phonebook_id}/downloads")
async def post_phone_book():
    file = save_file("phonebook.csv", Phonebook.contacts)
    return FileResponse(path="phonebook.csv", filename="phonebook.csv")
