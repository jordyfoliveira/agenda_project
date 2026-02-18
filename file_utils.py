import os

def load_contacts(file_path):
    contacts = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                name, phone = line.strip().split(",")
                contacts.append((name, phone))
    return contacts


def save_contacts(file_path, contacts):
    with open(file_path, "w", encoding="utf-8") as f:
        for name, phone in contacts:
            f.write(f"{name},{phone}\n")