import json
from dataclasses import asdict
from typing import List, Optional

import app.persistence as p
from app.persistence import Contact
from .contacts_service_boundary import ContactInput, ContactOutput, UpdateContactInput


def fetch_all_contacts() -> list[ContactOutput]:
    return [ContactOutput(**asdict(contact)) for contact in p.fetch_all_contacts()]


def search_contacts(query: str) -> List[ContactOutput]:
    def search_name(contact: Contact) -> bool:
        return query.lower() in contact.name.lower()

    def search_phone(contact: Contact) -> bool:
        return query.lower() in contact.phone.lower()

    return [ContactOutput(**asdict(contact))
            for contact in p.fetch_all_contacts() if search_name(contact) or search_phone(contact)]


def add_contact(contact: ContactInput) -> ContactOutput:
    return ContactOutput(**asdict(p.persist_contact(Contact(**asdict(contact)))))


def delete_contact(id: str) -> bool:
    return p.delete_contact(id)


def update_contact(id: str, contact: UpdateContactInput) -> Optional[ContactOutput]:
    existing_contact = p.fetch_contact(id)
    if existing_contact is None:
        return None
    existing_contact.name = contact.name if contact.name else existing_contact.name
    existing_contact.phone = contact.phone if contact.phone else existing_contact.phone
    existing_contact.email = contact.email if contact.email else existing_contact.email
    persisted_contact = p.persist_contact(existing_contact)
    return ContactOutput(**asdict(persisted_contact))


def import_contacts(serialized_contacts: str) -> list[tuple[ContactOutput, ContactOutput]]:
    contacts = [ContactOutput(**serialized_contact) for serialized_contact in json.loads(serialized_contacts)]
    existing_contact_ids = set(p.fetch_all_contact_ids())
    new_contacts = [contact for contact in contacts if contact.id not in existing_contact_ids]
    for contact in new_contacts:
        p.persist_contact(Contact(**asdict(contact)))
    return [
        (contact, ContactOutput(**asdict(p.fetch_contact(contact.id))))
        for contact in contacts if contact.id in existing_contact_ids
    ]


def import_selected_contacts(selected_contacts: list[ContactOutput]) -> None:
    for contact in selected_contacts:
        p.persist_contact(Contact(**asdict(contact)))


def export_contacts(ids: Optional[list[str]]) -> str:
    contacts = [p.fetch_contact(id) for id in ids] if ids is not None else p.fetch_all_contacts()
    contact_outputs = [ContactOutput(**asdict(contact)) for contact in contacts if contact is not None]
    return json.dumps([asdict(contact_output) for contact_output in contact_outputs])
