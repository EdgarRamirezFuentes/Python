from domain.Movie import Movie
from service.Catalog import Catalog
from os import system

option = None 

def clearTerminal():
    try:
        system("clear") ## Mac and Linux
    except Exception as e:
        system("cls") ## Windows

while True:
    clearTerminal()
    print("1 - Add Movie")
    print("2 - List the movies")
    print("3 - Delete the catalog")
    print("4 - Exit")
    option = input("Input your choice: ")
    if(option == "1"):
        clearTerminal()
        name = input("Input the name of the movie: ")
        newMovie = Movie(name)
        Catalog.addMovie(newMovie)
    elif option == "2":
        clearTerminal()
        print("Movies:\n")
        Catalog.listMovies()
        option = input("\nPress enter to continue...")
    elif option == "3":
        clearTerminal()
        Catalog.deleteCatalog()
        option = input("Catalog deleted\nPress enter to continue...")
    else:
        break;