class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    
    def getAncho(self):
        return self.__ancho
    
    def getAlto(self):
        return self.__alto
    
    def setAncho(self, ancho):
        self.__ancho = ancho
    
    def setAlto(self, alto):
        self.__alto = alto
        
    def __str__(self):
        return "Ancho: " + str(self.__ancho) + " Alto: " + str(self.__alto)