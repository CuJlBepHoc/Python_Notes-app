from note_operations import create_note, read_notes, edit_note, delete_note


def main():
    while True:
        print("\n1. Создать заметку")
        print("2. Показать все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            note = create_note()
            print("Заметка успешно сохранена")
        elif choice == '2':
            notes = read_notes()
            if notes:
                for i, note in enumerate(notes):
                    print(f"{i}. Заголовок: {note['title']}, Дата создания: {
                          note['timestamp']}")
            else:
                print("Список заметок пуст")
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note
        elif choice == '5':
            break
        else:
            print("Некорректный выбор")


if __name__ == "__main__":
    main()
