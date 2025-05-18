from classes.user import User
from classes.book import Book
from type_enum.type_livre import TypeLivre
import jsonpickle

class Library:
    def __init__(self):
        self.lst_user = []
        self.lst_livre = []


    def add_book(self,livre):
        self.load()
        self.lst_livre.append(livre)
        self.sauvegarder()

    def add_user(self,user):
        self.load()
        self.lst_user.append(user)
        self.sauvegarder()

    def sauvegarder(self):
        with open('library.json', 'w',encoding="utf-8") as file:
            file.write(jsonpickle.encode(self,indent=4))

    @staticmethod
    def load():
        try:
            with open('library.json', 'r', encoding="utf-8") as file:
                return jsonpickle.decode(file.read())
        except FileNotFoundError:
            return []


library  = Library()
larcel  = User("larcel",12)
eliena = User("eliena",19)

book1 = Book("allltak","yea",TypeLivre.REFERENCE)
book2 = Book("beyblade","asd",TypeLivre.FICTION)
book3 = Book("bakugan","asd",TypeLivre.NONFICTION)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)



library.load()

larcel.retourner_livre()


library.add_user(larcel)
library.sauvegarder()