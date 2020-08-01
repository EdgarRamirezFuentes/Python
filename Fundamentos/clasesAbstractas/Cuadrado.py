from clasesAbstractas.FiguraGeometrica import FiguraGeometrica

class Cuadrado (FiguraGeometrica):
    def __init__(self, w, c):
        super().__init__(w, w, c)
    
    def area(self):
        return self.getH() * self.getW()
    
    def __str__(self):
        return "Área: " + str(self.area()) + " Color: " + self.getC()