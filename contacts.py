from file_utils import load_contacts, save_contacts

FILE_PATH = "contacts.txt"

def add_contact_cli(name: str, phone: str):
    contacts = load_contacts(FILE_PATH)
    if any(n.lower() == name.lower() for n, _ in contacts):
        print("Contacto já existe.")
        return

    contacts.append((name.strip(), phone.strip()))
    save_contacts(FILE_PATH, contacts)
    print("Contacto adicionado com sucesso.")

def list_contacts_cli():
    contacts = load_contacts(FILE_PATH)
    if not contacts:
        print("Sem contactos.")
        return
    for name, phone in contacts:
        print(f"{name} | {phone}")

def search_contact_cli(query: str):
    contacts = load_contacts(FILE_PATH)
    q = query.lower().strip()
    matches = [(n, p) for n, p in contacts if q in n.lower()]
    if not matches:
        print("Contacto não encontrado.")
        return
    for name, phone in matches:
        print(f"Encontrado -> {name} | {phone}")

def edit_contact_cli(name: str, new_phone: str):
    contacts = load_contacts(FILE_PATH)
    target = name.lower().strip()

    for i, (n, p) in enumerate(contacts):
        if n.lower() == target:
            contacts[i] = (n, new_phone.strip())
            save_contacts(FILE_PATH, contacts)
            print("Contacto atualizado.")
            return

    print("Contacto não encontrado.")

def delete_contact_cli(name: str):
    contacts = load_contacts(FILE_PATH)
    target = name.lower().strip()

    new_contacts = [(n, p) for n, p in contacts if n.lower() != target]
    if len(new_contacts) == len(contacts):
        print("Contacto não encontrado.")
        return

    save_contacts(FILE_PATH, new_contacts)
    print("Contacto removido.")