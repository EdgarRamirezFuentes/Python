import os
class Catalog:
    catalogPath = "./catalogoPeliculas/MovieCatalog.txt"
    def __init__(self):
        pass
    @staticmethod
    def addMovie(movie):
        try:
            archivo = open(Catalog.catalogPath, "a")
            archivo.write(movie.getName() + "\n")
        except Exception as e:
            print(e)
        finally:
            archivo.close()
            
    @staticmethod
    def listMovies():
        try:
            archivo = open(Catalog.catalogPath, "r")
            movies = archivo.readlines()
            for movie in movies:
                print("* " + movie,end='')
        except Exception as e:
            print(e)
        finally:
            archivo.close()
    
    @staticmethod
    def deleteCatalog():
        try:
            os.remove(Catalog.catalogPath)
        except Exception as e:
            print(e)