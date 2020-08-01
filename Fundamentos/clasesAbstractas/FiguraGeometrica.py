
## ! No se pueden crear objetos de clases abstractas.

## * Se necesita importar para poder crear clases abstractas.

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, w , h, c):
        self.__w = w
        self.__h = h
        self.__c = c
    
    def getW(self):
        return self.__w 
    
    def getH(self):
        return self.__h
    
    def getC(self):
        return self.__c 
    
    def setW(self, w):
        self.__w = w
        
    def setH(self, h):
        self.__h = h
        
    def setC(self, c):
        self.__c = c
            
    ## * Este decorador hace que este método se vuelva abstacto.
    ## ! Con un solo método abstracto, toda la clase se vuelve abstracta.
    @abstractmethod
    def area(self):
        pass