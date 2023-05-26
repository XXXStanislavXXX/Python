from functional import *
from interface import start

path = "phone_book.txt"

start()

actions = {"1": "list",
           "2": "record",
           "3": "search",
           "4": "change",
           "5": "delete",
           "q": "quit"}
action = None

while action != "q":
    print("What should i do?", *[f"{i} - {actions[i]}" for i in actions])
    action = input()
    while action not in actions:
        print("What should i do?", *[f"{i} - {actions[i]}" for i in actions])
        action = input()
        if action not in actions:
            print("Data incorrect")
    if action != "q":
        if action == "1":
            print_records(path)
        elif action == "2":
            input_records(path)
        elif action == "3":
            find_records(path, *find_char())
        elif action == "4":
            change_records(path)
        elif action == "5":
            delete_records(path)