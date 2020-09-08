from loggerBase import logger

class Person:
    def __init__(self, idPerson= None, name="",  email=""):
        self.__idPerson = idPerson
        self.__name = name
        self.__email = email 
    
    ## Getters
    def getID(self):
        return self.__idPerson
    def getName(self):
        return self.__name
    def getEmail(self):
        return self.__email
    
    ## Setters
    def setName(self, name):
        self.__name = name
    def setEmail(self, email):
        self.__email = email 
    
    def __str__(self):
        return(
            f'ID: {self.__idPerson} '
            f'Name: {self.__name} '
            f'Email: {self.__email} '
        )