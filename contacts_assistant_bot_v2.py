def input_errors(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return f'ValueError: {ve}, change input, please.'
        except KeyError as ke:
            return f'KeyError: {ke}, change input, please.'
        except IndexError as ie:
            return f'IndexError: {ie}, change input, please.'
        except Exception as e:
            return f'Unknown error: {e}, {type(e)}'
    return inner


@input_errors
def parse_validate_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_errors
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        what_to_do = input(f'Contact {name} already exists. Replace?: ')
        match what_to_do.lower():
            case 'y' | 'yes' | 1:
                contacts[name] = phone
                return 'Contact replaced.\n'
            case _:
                return 'Adding canceled.\n'
    contacts[name] = phone
    return 'Contact added.\n'


@input_errors
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise ValueError(f'No name {name} in contacts')
    contacts[name] = phone
    return 'Contact changed.\n'


@input_errors
def show_all(contacts):
    result = ''
    for name, phone in contacts.items():
        result += f'{name}: {phone}\n'
    return result


@input_errors
def show_phone(args, contacts):
    result = ''
    name = args[0]
    if name not in contacts:
        raise ValueError(f'No name {name} in contacts')
    result = f'{name}: {contacts[name]}\n'
    return result


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_validate_input(user_input)
        match command:
            case 'close' | 'exit' | 'quit' | 'q':
                print('Good bye!')
                break
            case 'hello':
                print('How can I help you?\n')
            case  'add':
                print(add_contact(args, contacts))
            case 'change':
                print(change_contact(args, contacts))
            case 'all':
                print(show_all(contacts))
            case 'phone':
                print(show_phone(args, contacts))
            case _:
                print('Invalid command.\n')


if __name__ == '__main__':
    main()
