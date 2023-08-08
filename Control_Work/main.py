import json
import os
import time
import datetime
from datetime import datetime

# Путь к файлу с заметками
file_path = 'notes.json'


# Функция для чтения заметок из файла
def read_notes():
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            notes = json.load(f)
        return notes
    else:
        return {}


# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(file_path, 'w') as f:
        json.dump(notes, f, indent=4)


# Функция для добавления заметки
def add_note():
    notes = read_notes()
    note_id = len(notes) + 1
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    timestamp = time.time()
    notes[note_id] = {'title': title, 'body': body, 'timestamp': timestamp}
    save_notes(notes)
    print('Заметка успешно добавлена')


# Функция для удаления заметки
def delete_note():
    notes = read_notes()
    note_id = input('Введите идентификатор заметки: ')
    if note_id not in notes:
        print('Заметка с таким идентификатором не найдена')
        return
    del notes[note_id]
    save_notes(notes)
    print('Заметка успешно удалена')


# Функция для редактирования заметки
def edit_note():
    notes = read_notes()
    note_id = input('Введите идентификатор заметки: ')
    if note_id not in notes:
        print('Заметка с таким идентификатором не найдена')
        return
    title = input('Введите новый заголовок (оставьте пустым, если не хотите менять): ')
    body = input('Введите новый текст (оставьте пустым, если не хотите менять): ')
    if title:
        notes[note_id]['title'] = title
    if body:
        notes[note_id]['body'] = body
    notes[note_id]['timestamp'] = time.time()
    save_notes(notes)
    print('Заметка успешно изменена')


# Функция для печати заметки
def print_note(note_data, note_id):
    print('Заметка №:', note_id)
    print('Заголовок:', note_data['title'])
    print('Текст:', note_data['body'])
    print('Дата создания/изменения:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(note_data['timestamp'])))
    print()


# Функция для вывода списка всех заметок
def list_notes_date():
    date_input = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    notes = read_notes()
    for note_id, note_data in notes.items():
        try:
            date_filter = datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError:
            print('Неверный формат даты. Используйте формат ГГГГ-ММ-ДД (например, 2023-07-19)')
            return

        note_date = datetime.fromtimestamp(note_data['timestamp']).date()

        if note_date == date_filter:
            print_note(note_data, note_id)


def list_notes():
    notes = read_notes()
    for note_id, note_data in notes.items():
        print_note(note_data, note_id)


# Функция для чтения конкретной заметки по идентификатору
def read_note():
    notes = read_notes()
    note_id = input('Введите идентификатор заметки: ')
    if note_id not in notes:
        print('Заметка с таким идентификатором не найдена')
        return
    note_data = notes[note_id]
    print_note(note_data, note_id)


def main():
    while True:
        print('Выберите действие:')
        print('1. Добавить заметку')
        print('2. Удалить заметку')
        print('3. Редактировать заметку')
        print('4. Вывести список заметок по дате')
        print('5. Просмотреть заметку')
        print('6. Вывести весь список заметок')
        print('7. Выход')
        choice = input('Введите номер действия: ')
        if choice == '1':
            add_note()
        elif choice == '2':
            delete_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            list_notes_date()
        elif choice == '5':
            read_note()
        elif choice == '6':
            list_notes()
        elif choice == '7':
            return
        else:
            print(f'Команды {choice} не существует.')


main()