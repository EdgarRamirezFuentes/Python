class Rectangle:
    ## Constuctor
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    ## Getters
    def getBase(self):
        return self.base

    def getHeight(self):
        return self.height
    
    ## Setters
    
    def setBase(self, base):
        self.base = base
        
    def setHeight(self, height):
        self.height = height
        
    ## Methods
    
    def area(self):
        return self.base * self.height 
    
    

base = int(input("Insert the length of the base of the rectangle: "))
height = int(input("Insert the length of the height of the rectangle: "))
rectangle = Rectangle(base,height)
print(rectangle.getBase())
print(rectangle.getHeight())
print(rectangle.area())
rectangle.setBase(5)
rectangle.setHeight(8)
print(rectangle.area())