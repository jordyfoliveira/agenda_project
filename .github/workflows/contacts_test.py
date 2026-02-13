import unittest
import os
from contacts import add_contact, search_contact, edit_contact, delete_contact
from file_utils import load_contacts, save_contacts

# Vamos usar um ficheiro de teste
TEST_FILE = "contacts_test.txt"

# Helper para resetar ficheiro
def reset_file():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    save_contacts(TEST_FILE, [])

# Mock das funções para usar TEST_FILE
def add_contact_mock(name, phone):
    contacts = load_contacts(TEST_FILE)
    for n, _ in contacts:
        if n.lower() == name.lower():
            return False
    contacts.append((name, phone))
    save_contacts(TEST_FILE, contacts)
    return True

def search_contact_mock(name):
    contacts = load_contacts(TEST_FILE)
    results = [ (n,p) for n,p in contacts if name.lower() in n.lower() ]
    return results

def edit_contact_mock(name, new_phone):
    contacts = load_contacts(TEST_FILE)
    for i, (n, p) in enumerate(contacts):
        if n.lower() == name.lower():
            contacts[i] = (n, new_phone)
            save_contacts(TEST_FILE, contacts)
            return True
    return False

def delete_contact_mock(name):
    contacts = load_contacts(TEST_FILE)
    new_contacts = [c for c in contacts if c[0].lower() != name.lower()]
    if len(new_contacts) == len(contacts):
        return False
    save_contacts(TEST_FILE, new_contacts)
    return True

# ==============================
# Testes
# ==============================
class TestContacts(unittest.TestCase):

    def setUp(self):
        reset_file()  # limpa antes de cada teste

    def test_add_contact(self):
        self.assertTrue(add_contact_mock("Ana", "912345678"))
        self.assertFalse(add_contact_mock("Ana", "999999999"))  # duplicado

    def test_search_contact(self):
        add_contact_mock("Ana", "912345678")
        add_contact_mock("Bruno", "934567890")
        results = search_contact_mock("an")
        self.assertEqual(len(results), 1)
        results2 = search_contact_mock("b")
        self.assertEqual(len(results2), 1)

    def test_edit_contact(self):
        add_contact_mock("Ana", "912345678")
        self.assertTrue(edit_contact_mock("Ana", "999999999"))
        self.assertFalse(edit_contact_mock("Bruno", "123456789"))  # não existe

    def test_delete_contact(self):
        add_contact_mock("Ana", "912345678")
        add_contact_mock("Bruno", "934567890")
        self.assertTrue(delete_contact_mock("Ana"))
        self.assertFalse(delete_contact_mock("Carlos"))  # não existe

if __name__ == "__main__":
    unittest.main()