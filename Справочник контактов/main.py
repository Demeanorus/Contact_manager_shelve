from contact_actions import *


def display_menu():
    print("1 - Добавить контакт")
    print("2 - Просмотреть контакт")
    print("3 - Редактировать контакт")
    print("4 - Удалить контакт")
    print("5 - Показать все контакты")
    print("6 - Выход")


def main():
    while True:
        display_menu()
        choice = input("Выберите действие : ")
        if choice == "1":
            add_contact_action()
        elif choice == "2":
            view_contact_action()
        elif choice == "3":
            edit_contact_action()
        elif choice == "4":
            delete_contact_action()
        elif choice == "5":
            list_all_contacts_action()
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
