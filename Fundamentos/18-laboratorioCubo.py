class Cube:
    
    ## Constructor
   
    def __init__(self, large, height, width):
        self.large = large
        self.height = height
        self.width = width
    
    ## Getters
    
    def getLarge(self):
        return self.large
    
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    ## Setters
    
    def setLarge(self, large):
        self.large = large
        
    def setHeight(self, height):
        self.height = height
    
    def setWidth(self, width):
        self.width = width
        
    ## Methods
    
    def volume(self):
        return self.large * self.width * self.height