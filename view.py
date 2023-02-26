class View(object):

    # @staticmethod
    # def show_list(notes):
    #     for note in notes:
    #         print(note)

    @staticmethod
    def show_title_notes(notes):
        for note in notes:
            print(note.id, note.title)

    @staticmethod
    def show_note(note):
        print(note)

    @staticmethod
    def show_empty_list_message():
        print('Cписок заметок пустой!')

    @staticmethod
    def display_note_id_not_exist(search_id):
        print('Заметка с id: {} не найдена!'.format(search_id))

    @staticmethod
    def display_note_stored():
        print('Заметка успешно добавлена!')

    @staticmethod
    def display_note_updated(note_id):
        print('Заметка с id:{} обновлена успешно!' .format(note_id))

    @staticmethod
    def display_note_deletion(note_id):
        print('Удаление заметки с id: {} выполнено!'.format(note_id))

    # def display_all_notes_deletion():
    #     print('Все заметки удалены!')
