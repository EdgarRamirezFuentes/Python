class Monitor:
    quatity = 0
    
    def __init__(self, name, brand, price, size):
        Monitor.quatity += 1
        self.__id = Monitor.quatity
        self.__name = name
        self.__brand = brand
        self.__price = price
        self.__size = size
    
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
        
    def getID(self):
        return self.__id
    
    def getSize(self):
        return self.__size
    
    def setSize(self, size):
        self.__size = size
    
    def __str__(self):
        return (
            f"Monitor:\n"
            f"ID: {str(self.getID())}\n"
            f"Name: {self.getName()}\n"
            f"Brand: {self.getBrand()}\n"
            f"Size: {self.getSize()}\n"
            f"Price: ${str(self.getPrice())}\n"
        )