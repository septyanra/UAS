from core.baseapp import BaseApp
from data_model import book
from data_model.book import Book


class MainApp(BaseApp):
    def __init__(self):
        self.books = []
        self.InputBook = []
        self.ViewBook = []
        BaseApp.__init__(self)
class ViewBook(Book) :
    def __init__(self):
        vBook = ViewBook(self, book)
        vBook.list_book()


if __name__ == "__main__":
    app = MainApp()
    app.run()

    @property
    def list_book(self):
        return self.list_book
    def add_book(self):
        return self.add_book()

