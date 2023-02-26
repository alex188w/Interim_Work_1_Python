from note import Note


class Presenter(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    # def show_notes(self):
    #     notes = self.model.read_notes()
    #     self.view.show_list(notes)

    def show_title_notes(self):
        notes = self.model.read_notes()
        self.view.show_title_notes(notes)

    def show_note(self, note_id):
        note = self.model.read_note(note_id)
        self.view.show_note(note)

    def create_note(self, note):
        self.model.create_note(note)
        self.view.display_note_stored()

    def update_note(self, note_id, date, title, text):
        self.model.update_note(note_id, date, title, text)
        self.view.display_note_updated(note_id)

    def delete_note(self, note_id):
        self.model.delete_note(note_id)
        self.view.display_note_deletion(note_id)

    # def delete_all_notes(self):
    #     self.model.delete_all_notes()
    #     self.view.display_all_notes_deletion()

    def notes_exist(self):
        notes = self.model.read_notes()
        if len(notes) == 0:
            self.view.show_empty_list_message()
            return False
        else:
            return True

    def note_id_exist(self, search_id):
        notes = self.model.read_notes()
        count = 0
        for note in notes:
            if note.id == search_id:
                count += 1
        if count != 0:
            return True
        else:
            self.view.display_note_id_not_exist(search_id)
            return False
