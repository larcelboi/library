from classes.book import Book
from type_enum.type_livre import TypeLivre

class User:
    def __init__(self,name:str,age:int):

        self.name = name
        self.age = age
        self.lst_livre = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nouv_name):
        if isinstance(nouv_name, str) and nouv_name.strip() !="":
            self._name = nouv_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, nouv_age):
        if isinstance(nouv_age, int):
            self._age = nouv_age

    def ajouter_livre(self):
            from classes.library import library

            library.load()
            nom = input("Nom de l'auteur du livre à réserver: ")
            titre = input("Titre du livre à réserver: ")

            if len(self.lst_livre) >= 4:
                print("Il n'y a plus de place dans la liste (max 4 livres).")
                return None

            for livre in library.lst_livre:
                if livre.author == nom and livre.title == titre:
                    print(f"Le livre '{livre.title}' de {livre.author} a été ajouté.")
                    return livre

            print("Livre non trouvé.")
            return None

    def retourner_livre(self):

        for livre in self.lst_livre:
            print(livre.author)
        livre_nom = input("Entrer le nom du livre : ").strip()
        dans_le_livre = False
        for livre in self.lst_livre:
            if livre.author == livre_nom:
                self.lst_livre.remove(livre)
                print(f"le livre {livre.author} a été enlevé")
                dans_le_livre = True
                break
        if not dans_le_livre:
            print(f"Vous n'avez aucun livre nommé {livre_nom}")


    def __str__(self):
        return f"Nom: {self.name} - Age: {self.age} - Livre: {self.lst_livre}"

