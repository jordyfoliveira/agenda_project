import argparse
from contacts import (
    add_contact_cli,
    search_contact_cli,
    edit_contact_cli,
    delete_contact_cli,
    list_contacts_cli,
)

def build_parser():
    parser = argparse.ArgumentParser(prog="agenda", description="Gestor de contactos (CLI)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Adicionar contacto")
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--phone", required=True)

    p_search = sub.add_parser("search", help="Procurar contacto (parcial)")
    p_search.add_argument("--name", required=True)

    p_edit = sub.add_parser("edit", help="Editar telefone de um contacto")
    p_edit.add_argument("--name", required=True)
    p_edit.add_argument("--phone", required=True)

    p_delete = sub.add_parser("delete", help="Apagar contacto")
    p_delete.add_argument("--name", required=True)

    sub.add_parser("list", help="Listar todos os contactos")

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_contact_cli(args.name, args.phone)

    elif args.command == "search":
        search_contact_cli(args.name)

    elif args.command == "edit":
        edit_contact_cli(args.name, args.phone)

    elif args.command == "delete":
        delete_contact_cli(args.name)

    elif args.command == "list":
        list_contacts_cli()

if __name__ == "__main__":
    main()