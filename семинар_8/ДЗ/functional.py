path = "phone_book.txt"
def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')

def input_records(file_name: str):
    with open(file_name, 'r+', encoding='utf-8') as data:
        record_id = 0
        for line in data:
            if line != '':
                record_id = line.split(';', 1)[0]
        print('Enter FCS thru space')
        line = f'{int(record_id) + 1};' + ';'.join(input().split()[:4]) + ';\n'
        confirm = confirmation('add record')
        if confirm == 'y':
            data.write(line)

def find_char():
    print('Choose char: ')
    print('0 - id, 1 - second name, 2 - name, 3 - third name, 4 - number, q - quit')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 'q'):
        print('Data incorrect')
        print('Choose char: ')
        print('0 - id, 1 - second name, 2 - first name, 3 - third name, 4 - number, q - quit')
        char = input()
    if char != 'q':
        inp = input('inter value\n')
        return char, inp
    else:
        return 'q', 'q'

def find_records(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Nothing found")
        return printed

def check_id_record(file_name: str, text: str):
    decision = input(f'D u know id? {text}? 1 - yes, 2 - no, q - quit\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Data incorrect')
        else:
            find_records(path, *find_char())
        decision = input(f'D u know id? {text}? 1 - yes, 2 - no, q - quit\n')
    if decision == '1':
        record_id = input('enter id, q - quit\n')
        while not find_records(file_name, '0', record_id) and record_id != 'q':
            record_id = input('enter id, q - quit\n')
        return record_id
    return decision

def confirmation(text: str):
    confirm = input(f"Confirm {text} record: y - yes, n - no\n")
    while confirm not in ('y', 'n'):
        print('Data incorrect')
        confirm = input(f"Confirm {text} record: y - yes, n - no\n")
    return confirm

def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)

def change_records(file_name: str):
    record_id = check_id_record(file_name, 'change')
    if record_id != 'q':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Enter FCS thru space\n').split()[:4]) + ';\n'
        confirm = confirmation('change')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)

def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'delete')
    if record_id != 'q':
        confirm = confirmation('change')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')

