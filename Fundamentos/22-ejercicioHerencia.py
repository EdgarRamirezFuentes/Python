class Vehicle:
    
    ## Constructor
    def __init__(self, color, wheels):
        self.__color = color
        self.__wheels = wheels
    
    ## Getters
    def getColor(self):
        return self.__color
    
    def getWheels(self):
        return self.__wheels
    
    ## Setters
    def setColor(self, color):
        self.__color = color
        
    def setWheels(self, wheels):
        self.__wheels = wheels
    
    def __str__(self):
        return "Color: " + self.__color + str(self.__wheels)
    
class Car(Vehicle):
    
    ## Constructor
    def __init__(self, color, wheels, speed):
        super().__init__(color, wheels)
        self.__speed = speed
    
    ## Getters
    
    def getColor(self):
        return super().getColor()
    
    def getWheels(self):
        return super().getWheels()
    
    def getSpeed(self):
        return self.__speed
    
    ## Setters
    
    def setColor(self, color):
        super().setColor(color)
        
    def setWheels(self, wheels):
        super().setWheels(wheels)
        
    def setSpeed(self, speed):
        self.__speed = speed
    
    def __str__(self):
        return super().__str__() + "Speed: " + str(speed)
    
class Bicycle(Vehicle):
    
    ## Constructor
    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.__type = type
    
    ## Getters
    
    def getColor(self):
        return super().getColor()
    
    def getWheels(self):
        return super().getWheels()
    
    def getType(self):
        return self.__type
    
    ## Setters
    
    def setColor(self, color):
        super().setColor(color)
        
    def setWheels(self, wheels):
        super().setWheels(wheels)
        
    def setType(self, type):
        self.__type = type
        
    def __str__(self):
        return super().__str__() + "Type: " + self.__type
        