from note_operations import create_note, read_notes, edit_note, delete_note
from utils import filter_notes_by_date


def show_notes(notes):
    if notes:
        for i, note in enumerate(notes, start=1):
            print(f"{i}. Заголовок: {note['title']}, Дата создания: {note['timestamp']}")
    else:
        print("Список заметок пуст")


def main():
    while True:
        print("\n1. Создать заметку")
        print("2. Показать все заметки")
        print("3. Прочитать заметку")
        print("4. Найти заметки по дате")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("9. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            note = create_note()
            print("Заметка успешно сохранена")
        elif choice == '2':
            show_notes(read_notes())
        elif choice == '3':
            index = int(input("Введите номер заметки для просмотра: "))
            notes = read_notes()
            if 1 <= index <= len(notes):
                note = notes[index - 1]
                print(f"{index}. Заголовок: {note['title']}, Дата создания: {note['timestamp']}")
                print("Тело заметки:", note['message'])
            else:
                print("Некорректный номер заметки")
        elif choice == '4':
            date = input("Введите дату в формате YYYY-MM-DD: ")
            show_notes(filter_notes_by_date(date))
        elif choice == '5':
            edit_note()
        elif choice == '6':
            delete_note()
        elif choice == '9':
            break
        else:
            print("Некорректный выбор")


if __name__ == "__main__":
    main()
