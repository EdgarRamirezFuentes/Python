from abc import abstractmethod

class InputDevice:
    def __init__(self, name, price, brand):
        self.__name = name
        self.__price = price
        self.__brand = brand
        
    @abstractmethod    
    def abstract(self):
        pass
    
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getBrand(self):
        return self.__brand
    
    def setName(self, name):
        self.__name = name
        
    def setBrand(self, brand):
        self.__brand = brand
        
    def setPrice(self, price):
        self.__price = price
        