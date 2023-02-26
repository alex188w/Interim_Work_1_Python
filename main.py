import datetime
from modelNotes import ModelNotes
from presenter import Presenter
from note import Note
from view import View


def main():
    p = Presenter(ModelNotes("notes.json"), View())

    print("Введите команду:")
    print("1 - добавить заметку")
    print("2 - прочитать список заголовков заметок c номером id")
    print("3 - найти заметку по номеру id")
    print("4 - редактировать заметку по номеру id")
    print("5 - удалить заметку")
    print("Выйти из меню - нажмите <Enter>")

    try:
        while True:
            user_choise = int(input())
            if user_choise == 1:
                p.create_note(note_input())
            elif user_choise == 2:
                p.show_title_notes()
            elif user_choise == 3:
                note_id = int(
                    input("Введите номер id заметки, которую хотите найти:"))
                if p.note_id_exist(note_id) == True:
                    p.show_note(note_id)
            elif user_choise == 4:
                note_id = int(
                    input("Введите номер id заметки, которую хотите редактировать:"))
                if p.note_id_exist(note_id) == True:
                    date = datetime.datetime.now().strftime("%Y-%b-%d %H:%M")
                    title = input('Введите заголовок заметки: ')
                    text = input('Введите текст заметки: ')
                    p.update_note(note_id, date, title, text)
            elif user_choise == 5:
                note_id = int(
                    input("Введите номер id заметки, которую хотите удалить:"))
                if p.note_id_exist(note_id) == True:
                    p.delete_note(note_id)
            else:
                print("Число должно быть от одного до пяти")
    except ValueError:
        print("Выход из программы")


def note_input():
    id = 0
    date = datetime.datetime.now().strftime("%Y-%b-%d %H:%M")
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
    return Note(id, date, title, text)


if __name__ == "__main__":
    main()
