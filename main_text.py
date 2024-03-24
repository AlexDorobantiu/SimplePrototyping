import service as s
from service import ContactInput, ContactOutput, UpdateContactInput

if __name__ == "__main__":
    all_contacts: list[ContactOutput] = s.fetch_all_contacts()
    print("All contacts:", all_contacts)

    new_contact: ContactOutput = s.add_contact(ContactInput("Adi Shamir", "7890", "adi@adi.com"))
    print("New contact: ", new_contact)

    filtered_contacts: list[ContactOutput] = s.search_contacts("Sha")
    print("Search result: ", filtered_contacts)
    filtered_contacts: list[ContactOutput] = s.search_contacts("7890")
    print("Search result: ", filtered_contacts)

    exported_contacts = s.export_contacts(None)
    print("Export:", exported_contacts)

    updated_contact = s.update_contact(new_contact.id, UpdateContactInput(phone="0007890"))
    print("Updated contact:", updated_contact)

    import_contacts = s.import_contacts(exported_contacts)
    print("Imported:", import_contacts)

    s.import_selected_contacts([new_contact])
    print("Imported selected:", s.fetch_all_contacts())

    print("Deleted:", s.delete_contact(new_contact.id))
