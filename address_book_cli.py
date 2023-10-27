from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        if not (value.isdigit() and len(str(value)) == 10):
            raise ValueError('Invalid phone number.')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_num):
        self.phones.append(Phone(phone_num))

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return 'Phone successfully changed.'
        raise ValueError('Phone not found.')

    def remove_phone(self, phone_num):
        for item in self.phones:
            if str(item) == phone_num:
                self.phones.remove(item)
                return 'Phone removed.'
        raise ValueError('Phone not found.')

    def find_phone(self, phone_num):
        for phone in self.phones:
            if phone.value == phone_num:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        del self.data[name]


if __name__ == '__main__':

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    # Додаткові перевірки
    try:
        print(john_record.add_phone("98765432101"))
    except Exception as e:
        print(e)

    try:
        print(jane_record.add_phone("987654321"))
    except Exception as e:
        print(e)

    john.remove_phone('5555555555')
    print(john_record)
