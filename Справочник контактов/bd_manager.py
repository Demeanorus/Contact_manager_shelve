import shelve

BD_NAME = "contacts.db"

def open_storage():
    """Открывает базу и возвращает объект."""
    return shelve.open(BD_NAME, flag="c")


def get_all_contacts():
    """Возвращаем все контакты из базы"""
    db = None
    try:
        db = shelve.open(BD_NAME, flag="c")
        results = {}
        for name in db:
            results[name] = db[name]
        return results
    except Exception:
        return {}
    finally:
        try:
            db.close()
        except Exception:
            pass

def get_contact(name):
    """Возвращаем один контакт по имени"""
    if not name:
        return None
    db = None
    try:
        db = shelve.open(BD_NAME, flag='c')
        contact = db.get(name)
        return contact
    except Exception:
        return None
    finally:
        try:
            db.close()
        except Exception:
            pass


def add_contact(name, phone, email, address):
    """Добавляем новый контакт"""
    if not name:
        return False
    db = None
    try:
        db = shelve.open(BD_NAME, flag='c')
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
    finally:
        try:
            db.close()
        except Exception:
            pass

def update_contact(name, phone, email, address):
    """Обновляет существующий контакт"""
    if not name:
        return False
    db = None
    try:
        db = shelve.open(BD_NAME, flag='c')

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
    finally:
        try:
            db.close()
        except Exception:
            pass

def delete_contact(name):
    """Удаляет контакт по имени."""
    if not name:
        return False
    db = None
    try:
        db = shelve.open(BD_NAME, flag='c')
        if name not in db:
            return False
        del db[name]
        return True
    except Exception:
        return False
    finally:
        try:
            db.close()
        except Exception:
            pass
