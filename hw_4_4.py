def parse_input(user_input):
    cmd, *args = user_input.split()# розбиває user_input на команду/cmd (add, change, show_) та args (імя, телефон...)
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args #name[0] phone[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if args[0] in contacts.keys():
        add_contact(args, contacts)
        return("Contact changed")
    else:
        print(f"No such user {args[0]}")

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        print(f"No such user {name}")



def show_all(args, contacts):
    s = ""       #змінні (стрінг) для збереження та виведення всіх контактів
    for key in contacts:
        s+=(f"{key:10} : {contacts[key]:10}\n")  #поповнення списку з перенесенням на новий рядок(\n) та відступом (:10) пробілів
    return s


def main(): #функція комунікації?
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show": #виконання команди/функції show_phone
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(args, contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()