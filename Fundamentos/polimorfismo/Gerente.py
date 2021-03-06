from polimorfismo.Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.__departamento = departamento
        
    def getDepartamento (self):
        return self.__departamento
    
    def setDepartamento(self, departamento):
        self.__departamento = departamento
        
    def __str__(self):
        return super().__str__() + " Departamento: " + self.__departamento