import unittest
from datetime import datetime

import app.persistence as p
from app.persistence import Contact


class PersistencePerformanceTestCase(unittest.TestCase):

    def test_persistence_load_empty(self):
        time1 = datetime.now()
        all_contacts = p.fetch_all_contacts()
        time2 = datetime.now()
        print("Execution time: ", (time2 - time1).microseconds)
        self.assertEqual(len(all_contacts), 0)

    def test_persistence_create(self):
        time1 = datetime.now()
        p.bulk_persist_contacts([Contact(f'{i}', f"Name {i}", f"Phone {i}", f"Email {i}") for i in range(1000)])
        time2 = datetime.now()
        print("Execution time: ", (time2 - time1).microseconds)
        self.assertTrue(True)

    def test_persistence_load_1000(self):
        time1 = datetime.now()
        all_contacts = p.fetch_all_contacts()
        time2 = datetime.now()
        print("Execution time: ", (time2 - time1).microseconds)
        self.assertEqual(len(all_contacts), 1000)


if __name__ == '__main__':
    unittest.main()
