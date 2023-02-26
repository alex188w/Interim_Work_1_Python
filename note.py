class Note(object):
    def __init__(self, id: int, date: str, title: str, text: str):
        self.id = id
        self.date = date
        self.title = title
        self.text = text

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    def __str__(self):
        return f'\nЗаметка номер: {self._id}\nДата создания(редактирования):' \
            f' {self._date}\nЗаголовок заметки: {self._title}\nТекст заметки: {self._text}\n '
