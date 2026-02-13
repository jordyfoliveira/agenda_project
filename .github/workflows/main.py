from contacts import add_contact, search_contact, edit_contact, delete_contact
import sys

def menu():
    while True:
        print("\n===== AGENDA =====")
        print("1 - Adicionar")
        print("2 - Procurar")
        print("3 - Editar")
        print("4 - Apagar")
        print("5 - Sair")

        option = input("Escolha: ").strip()

        if option == "1":
            add_contact()
        elif option == "2":
            search_contact()
        elif option == "3":
            edit_contact()
        elif option == "4":
            delete_contact()
        elif option == "5":
            print("Até breve.")
            sys.exit(0)
        else:
            print("Opção inválida.")
            input("Prima ENTER para continuar...")

if __name__ == "__main__":
    menu()