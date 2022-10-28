from classbook import AddressBook
from classbook import Record

contacts = AddressBook()


def input_error(error):
    def wrapper(*args, **kwargs):
        try:
            return error(*args, **kwargs)
        except KeyError:
            return "Ви ввели не вірне ім'я"
        except IndexError:
            return "Потрібне ім'я та номер телефону"
        except ValueError as red:
            return red.args[0]

    return wrapper

@input_error
def first_step():
    return "How can I help you?"

@input_error
def add_contacts(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phones = new_data[1:]
    if name in contacts:
        raise ValueError("Дублікат імені")
    new_record = Record(name)

    for phone in phones:
        new_record.add_phone(phone)

    contacts.add_record(new_record)
    return f"Ви створили {name}:{phones}"

@input_error
def change_phones_funk(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phones = new_data[1:]
    if contacts.has_record(name):
        record = contacts.get_record(name)
        record.clear_phones()

        for phone in phones:
            record.add_phone(phone)

        return f"Для контакту {name} змінено номер на {phones}"
    return f"За даним {name} контакту не існує, зверніться до команди add "

@input_error
def find_phone(value):
    return contacts.search(value.strip()).get_info()

@input_error
def show_all_funk():
    contact = ""
    for name, record in contacts.get_all_records().items():
        contact += f"{record.get_info()}\n"
    return contact

@input_error
def quit_funk():  # Функція виходу з команд "good bye", "close", "exit".
    return "До наступної зустрічі"


@input_error
def del_funk(name):
    name = name.strip()
    if contacts.has_record(name):
        contacts.remove_record(name)
        return f"{name} видалено"
    raise ValueError (f"{name} знайти не вдалось")


COMMANDS = {
    "hello": first_step,
    "add": add_contacts,
    "change phones": change_phones_funk,
    "phone": find_phone,
    "show all": show_all_funk,
    "good bye": quit_funk,
    "close": quit_funk,
    "exit": quit_funk,
    "delete": del_funk
}

def return_func(data):
    return COMMANDS.get(data, error_func)

def error_func():
    return "Помилкова команда"

def edits(input_data):
    key_part = input_data
    data_part = ""
    for command in COMMANDS:
        if input_data.strip().lower().startswith(command):
            key_part = command
            data_part = input_data[len(key_part):]
            break
    if data_part:
        return return_func(key_part)(data_part)
    else:
        return return_func(key_part)()

def main():
    while True:
        user_input = input("Введіть команду: ")
        res = edits(user_input)
        print(res)
        if res == "До наступної зустрічі":
            break

if __name__ == "__main__":
    main()