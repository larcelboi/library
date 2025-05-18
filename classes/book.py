from type_enum.type_livre import TypeLivre

class Book:
    def __init__(self,author:str,title:str,genre:TypeLivre):
        self.author = author
        self.title = title
        self.genre = genre

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, nouv_author):
        if isinstance(nouv_author, str) and nouv_author.strip() !="":
            self._author = nouv_author
        else:
            raise ValueError("author must be a str and contain a name")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, nouv_title):
        if isinstance(nouv_title, str) and nouv_title.strip() != "":
            self._title = nouv_title
        else:
            raise ValueError("title must be a str and contain a name")

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, nouv_genre):
        if isinstance(nouv_genre,TypeLivre):
            self._genre = nouv_genre
        else:
            raise ValueError("genre book must be a type livre")

    def __str__(self):
        return f"Nom: {self.author} - Titre: {self.title} - Genre: {self.genre.value}"

