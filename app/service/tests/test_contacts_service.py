import unittest
from datetime import datetime

from app import service as c
from app.service import ContactInput


class ContactServiceTestCase(unittest.TestCase):
    def test_search(self):
        c1 = c.add_contact(ContactInput("Adi Shamir", "123-456-7890", ""))
        c2 = c.add_contact(ContactInput("Ronald Rivest", "123-456-7890", ""))
        c3 = c.add_contact(ContactInput("Andrew Yao", "123-456-7890", ""))
        time1 = datetime.now()
        search_result = c.search_contacts("Sha")
        time2 = datetime.now()
        print("Execution time: ", (time2 - time1).microseconds)
        self.assertEqual(len(search_result), 1)
        c.delete_contact(c1.id)
        c.delete_contact(c2.id)
        c.delete_contact(c3.id)

    def test_search_1000(self):
        contact_inputs = [ContactInput(f"Name {i}", f"Phone {i}", f"Email {i}") for i in range(1000)]
        contacts = [c.add_contact(contact_input) for contact_input in contact_inputs]
        time1 = datetime.now()
        search_result = c.search_contacts("777")
        time2 = datetime.now()
        print("Execution time: ", (time2 - time1).microseconds)
        self.assertEqual(len(search_result), 1)
        self.assertEqual(search_result[0].name, "Name 777")
        for contact in contacts:
            c.delete_contact(contact.id)


if __name__ == '__main__':
    unittest.main()
