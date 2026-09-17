import shelve

BD_NAME = "contacts.db"

def open_storage():
    """Открывает базу и возвращает объект."""
    return shelve.open(BD_NAME, flag="c")


def get_all_contacts():
    """Возвращаем все контакты из базы"""
    try:
        with open_storage() as db:
            results = {}
            for name in db:
                results[name] = db[name]
            return results
    except Exception:
        return {}


def get_contact(name):
    """Возвращаем один контакт по имени"""
    if not name:
        return None
    try:
        with open_storage() as db:
            contact = db.get(name)
            return contact
    except Exception:
        return None



def add_contact(name, phone, email, address):
    """Добавляем новый контакт"""
    if not name:
        return False
    try:
        with open_storage() as db:
            if name in db:
                return False
            db[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            return True
    except Exception:
        return False


def update_contact(name, phone, email, address):
    """Обновляет существующий контакт"""
    if not name:
        return False
    try:
        with open_storage() as db:
            if name not in db:
                return False
            db[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            return True
    except Exception:
        return False


def delete_contact(name):
    """Удаляет контакт по имени."""
    if not name:
        return False
    try:
        with open_storage() as db:
            if name not in db:
                return False
            del db[name]
            return True
    except Exception:
        return False
