from classes.book import Book
from classes.user import User
from classes.library import Library, library


def menu():
    library.creation_livre()
    while True:
        library.load()

        choix = input("""
        1.Voir livre 
        2.Créer un user
        3.Réerver livre 
        4.Retourner livre
        5.voir information user
        0.Quitter
        Entrer votre choix:
        """)

        match choix:
            case "1":
                voir_livre()
            case "2":
                 creation_user()
            case "3":
                if library.lst_user is not None:
                     reserver_livre()
                else:
                    print("il n'y a aucune personne dans la bibliothèque")
            case "4":
                retourner_livre()
            case "5":
                if library.lst_user is not None:
                    information_users()
                else:
                    print("il n'y a aucune personne dans la bibliothèque")
            case "0":
                print(f"Au revoir")
                break

            case _:
                print(f"choix invalide")


def voir_livre():
    library.voir_livre()

def creation_user():
    nom = input("Nom : ")
    age = int(input("Age : "))
    personne = User(nom,age)
    library.add_user(personne)
    print(personne.name,"a été ajouté dans la bibliothèque")

def reserver_livre():
    nom = input("Entrer le nom de la personne: ")
    joueur = None
    for personne in library.lst_user:
        if personne.name == nom:
            joueur = personne
            break
    if joueur is not None:
        print(f"Veuillez choisir un livre parmi ceci: ")
        library.voir_livre()
        joueur.ajouter_livre()
        library.sauvegarder()

def retourner_livre():
    pass

def information_users():
    library.informations_user()

if __name__ == "__main__":
    menu()