from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass

class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def get_info(self):
        phon_info = ""
        for phon in self.phones:
            phon_info += f"{phon.value}, "
        return f"{self.name.value} : {phon_info[:-2]}"

    def add_phone(self, phon):
        self.phones.append(Phone(phon))

    def change_phones(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)


    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all_records(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]


    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)

        for record in self.get_all_records().values():
            for phone in record.phones:
                if phone.value == value:
                    return record
        raise ValueError("Міскузі")
