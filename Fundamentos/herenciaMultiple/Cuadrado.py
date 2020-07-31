from herenciaMultiple.FiguraGeometrica import FiguraGeometrica
from herenciaMultiple.Color import Color
 
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
               
    def area(self):
        return self.getAncho() * self.getAlto()
    
    def __str__(self):
        return "Área: " + str(self.area()) + " Color: " + self.getColor()