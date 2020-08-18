class Computer:
    quantity = 0
    def __init__(self, name, monitor, mouse, keyboard, price):
        Computer.quantity += 1
        self.__id = Computer.quantity
        self.__name = name
        self.__monitor = monitor
        self.__mouse = mouse
        self.__keyboard = keyboard
        self.__price = price
    
    def getID(self):
        return self.__id
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price
    
    def getTotal(self):
        return self.__price + self.__monitor.getPrice() + self.__keyboard.getPrice() + self.__mouse.getPrice()   
    
    def __str__(self):
        return (
            f"Computer:\n"
            f"ID: {str(self.getID())}\n"
            f"Name: {self.getName()}\n"
            f"Price: ${str(self.getPrice())}\n\n"
            f"{self.__monitor.__str__()}\n"
            f"{self.__mouse.__str__()}\n"
            f"{self.__keyboard.__str__()}\n"
            f"Total: ${str(self.getTotal())}"
        )
