from classes.user import User
from classes.book import Book
from type_enum.type_livre import TypeLivre
import jsonpickle

class Library:
    def __init__(self):
        self.lst_user = []
        self.lst_livre = []

    def creation_livre(self):
        self.load()
        book1 = Book("beyblade","mrco",TypeLivre.FICTION)
        book2 = Book("babab","jaa",TypeLivre.REFERENCE)
        book3 = Book("totot","lalal",TypeLivre.NONFICTION)
        liste_livre = [book1,book2,book3]
        for livre in liste_livre:
            if not any(l.title == livre.title and l.author == livre.author for l in self.lst_livre):
                self.lst_livre.append(livre)
        self.sauvegarder()

    def enlever_livre(self,index_livre):
        self.load()
        self.lst_livre.pop(index_livre)
        self.sauvegarder()
    def informations_user(self):
        self.load()
        for personne in self.lst_user:
            print(personne)
    def voir_livre(self):
        self.load()
        for livre in self.lst_livre:
            print(livre)
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


    def load(self):
        try:
            with open('library.json', 'r', encoding="utf-8") as file:
                saved_library: Library = jsonpickle.decode(file.read())
                self.lst_user = saved_library.lst_user
                self.lst_livre = saved_library.lst_livre
        except FileNotFoundError:
            return []


library  = Library()
