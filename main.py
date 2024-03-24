from dataclasses import asdict

import service as s
from service import ContactInput
import rest_api_boundary as r

from fastapi import FastAPI

app = FastAPI()


@app.get("/contacts")
def fetch_contacts() -> list[r.ContactOutput]:
    return [r.ContactOutput(**asdict(contact)) for contact in s.fetch_all_contacts()]


@app.post("/contacts/add-contact")
def add_contact(add_contact_input: r.ContactInput) -> r.ContactOutput:
    return s.add_contact(ContactInput(**add_contact_input.dict()))
