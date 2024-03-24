__all__ = ['Contact', 'fetch_all_contacts', 'fetch_all_contact_ids', 'fetch_contact',
           'persist_contact', 'delete_contact', 'bulk_persist_contacts']

from .contacts_persistence_boundary import Contact
from .contacts_repository import fetch_all_contacts, fetch_all_contact_ids, \
    persist_contact, delete_contact, bulk_persist_contacts, fetch_contact
