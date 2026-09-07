import shelve

BD_NAME = "contacts.db"

def open_storage():
    """Открывает базу и возвращает объект."""
    return shelve.open(BD_NAME, flag="c")


def get_all_contacts():
    """Возвращаем все контакты из базы"""
    with shelve.open(BD_NAME, flag='c') as db:
        results = {}
        for name in db:
            results[name] = db[name]
        return results

def get_contact(name):
    """Возвращаем один контакт по имени"""
    with shelve.open(BD_NAME, flag='c') as db:
        return db.get(name)

def add_contact(name, phone, email, address):
    """Добавляем новый контакт"""
    with shelve.open(BD_NAME, flag='c') as db:
        if name in db:
            return False
        db[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        return True

def update_contact(name, phone, email, address):
    """Обновляет существующий контакт"""
    with shelve.open(BD_NAME, flag='c') as db:
        if name not in db:
            return False
        db[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        return True

def delete_contact(name):
    """Удаляет контакт по имени."""
    with shelve.open(BD_NAME, flag='c') as db:
        if name not in db:
            return False
        del db[name]
        return True

