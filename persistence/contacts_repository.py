import json
import uuid
from dataclasses import asdict
from pathlib import Path
from typing import Optional

from .contacts_persistence_boundary import Contact

DB_FOLDER = Path("db")
DB_PATH = DB_FOLDER / "contacts.json"

CONTACTS: Optional[dict[str, Contact]] = None


def _load_contacts() -> list[Contact]:
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r") as f:
        file_content = f.read()
        return [Contact(**contact) for contact in (json.loads(file_content))]


def _save_contacts(contacts: list[Contact]) -> None:
    DB_FOLDER.mkdir(parents=True, exist_ok=True)
    with open(DB_PATH, "w") as f:
        f.write(json.dumps([asdict(contact) for contact in contacts]))


def _populate_contacts():
    global CONTACTS
    if CONTACTS is None:
        contacts = _load_contacts()
        CONTACTS = {
            contact.id: contact for contact in contacts
        }


def _persist_contacts():
    global CONTACTS
    _save_contacts(list(CONTACTS.values()))


def persist_contact(contact: Contact) -> Contact:
    global CONTACTS
    _populate_contacts()
    if contact.id is None:
        contact.id = uuid.uuid4().hex[:4]
    CONTACTS[contact.id] = contact
    _persist_contacts()
    return contact


def bulk_persist_contacts(contacts: list[Contact]):
    _populate_contacts()
    global CONTACTS
    for contact in contacts:
        if contact.id is None:
            contact.id = uuid.uuid4().hex[:4]
        if contact.id in CONTACTS:
            raise ValueError(f"Contact with id {contact.id} already exists")
        CONTACTS[contact.id] = contact
    _persist_contacts()


def fetch_all_contacts():
    _populate_contacts()
    global CONTACTS
    return list(CONTACTS.values())


def fetch_all_contact_ids():
    _populate_contacts()
    global CONTACTS
    return list(CONTACTS.keys())


def fetch_contact(id: str) -> Optional[Contact]:
    _populate_contacts()
    global CONTACTS
    return CONTACTS.get(id)


def delete_contact(id: str) -> bool:
    _populate_contacts()
    global CONTACTS
    if id in CONTACTS:
        del CONTACTS[id]
        _persist_contacts()
        return True
    return False
