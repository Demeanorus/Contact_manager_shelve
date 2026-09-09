from bd_manager import *

def add_contact_action():
    """Добавление нового контакта"""
    name  = input("Введите имя контакта: ").strip()

    while True:
        phone = input("Введите телефон: ").strip()
        if is_valid_phone(phone):
            break
        print("Некорректный номер телефона. Попробуйте снова.")

    while True:
        email = input("Введите email: ").strip()
        if is_valid_email(email):
            break
        print("Некорректный Email. Попробуйте снова.")
    address = input("Введите адрес: ").strip()

    if add_contact(name, phone, email, address):
        print("Контакт успешно добавлен.")
    else:
        print("Контакт с таким именем существует.")


def view_contact_action():
    """Просмотр контактов"""
    name = input("Введите имя контакта: ").strip()
    contact = get_contact(name)

    if contact:
        print(f"Имя: {name}")
        print(f"Телефон: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Адрес: {contact['address']}")
    else:
        print("Контакт не найден.")


def edit_contact_action():
    """Редактирование контакта"""
    name = input("Введите имя контакта для редактирования: ").strip()
    contact = get_contact(name)

    if not contact:
        print("Контакт не найден.")
        return

    print("Оставьте поле пустым, если не хотите менять значение.")

    phone = input(f"Новый телефон ({contact['phone']}): ").strip() or contact['phone']
    email = input(f"Новый Email ({contact['email']}): ").strip() or contact['email']
    address = input(f"Новый адрес ({contact['address']}): ").strip() or contact['address']

    if update_contact(name, phone, email, address):
        print("Контакт успешно обновлен.")
    else:
        print("Ошибка обновления контакта.")



def delete_contact_action():
    """Удаление контакта"""
    name = input("Введите имя контакта для удаления: ").strip()

    if delete_contact(name):
        print("Контакт удален.")
    else:
        print("Контакт не найден.")

def list_all_contacts_action():
    """Вывод всех контактов"""
    contacts = get_all_contacts()

    if not contacts:
        print("Список контактов пуст.")
        return

    print("Все контакты:")
    for name, data in contacts.items():
        print(f"\nИмя: {name}")
        print(f"Телефон: {data['phone']}")
        print(f"Email: {data['email']}")
        print(f"Адрес: {data['address']}")

def is_valid_phone(phone: str) -> bool:
    """Проверка корректности телефона"""
    phone = phone.strip() # Убираем пробелы

    if not phone: # Проверка на пустую строку
        print("Это поле не должно быть пустым.")
        return False

    # Проверка на наличие +
    if phone.startswith("+"):
        digits = phone[1:]

        # После + должны идти только цифры
        if not digits.isdigit():
            return False

        if not (7 <= len(digits) <= 15):
            return False
        return True

    # Если строка начинается не с +, то она должна состоять из цифр
    if not phone.isdigit():
        return False

    if not (7 <= len(phone) <= 15):
        return False
    return True


def is_valid_email(email):
    """Проверка корректности email"""
    email = email.strip()
    if not email:
        return True

    if "@" not in email:
        return False

    local, _, domain = email.partition("@")

    if not local or not domain:
        return False

    if "." not in domain:
        return False

    if " " in email:
        return False

    forbidden = '()[]{}<>,"\'\\;:'
    if any(ch in forbidden for ch in email):
        return False
    return True


