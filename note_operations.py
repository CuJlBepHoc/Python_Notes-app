import json
import os
from datetime import datetime

# Функция для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите тело заметки: ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {'title': title, 'message': message, 'timestamp': timestamp}
    save_note(note)
    return note

# Функция для сохранения заметки в файле JSON
def save_note(note):
    if not os.path.exists('notes.json'):
        with open('notes.json', 'w') as file:
            json.dump([], file)
    with open('notes.json', 'r+') as file:
        data = json.load(file)
        data.append(note)
        file.seek(0)
        json.dump(data, file, indent=4)

# Функция для чтения всех заметок из файла JSON
def read_notes():
    if not os.path.exists('notes.json'):
        print("Список заметок пуст")
        return []
    with open('notes.json', 'r') as file:
        notes = json.load(file)
        return notes

# Функция для редактирования существующей заметки
def edit_note():
    notes = read_notes()
    if not notes:
        print("Список заметок пуст")
        return
    index = int(input("Введите номер заметки для редактирования: ")) - 1
    if 0 <= index < len(notes):
        notes[index] = create_note()
        with open('notes.json', 'w') as file:
            json.dump(notes, file, indent=4)
        print("Заметка успешно отредактирована")
    else:
        print("Некорректный номер заметки")

# Функция для удаления существующей заметки
def delete_note():
    notes = read_notes()
    if not notes:
        print("Список заметок пуст")
        return
    index = int(input("Введите номер заметки для удаления: ")) - 1
    if 0 <= index < len(notes):
        del notes[index]
        with open('notes.json', 'w') as file:
            json.dump(notes, file, indent=4)
        print("Заметка успешно удалена")
    else:
        print("Некорректный номер заметки")
