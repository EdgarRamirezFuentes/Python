class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def getNombre(self):
        return self.__nombre
    
    def  getEdad(self):
        return self.__edad
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setEdad(self, edad):
        self.__edad = edad 
        
    def __str__(self):
        return "Nombre: " + self.__nombre + " Edad: " + str(self.__edad)
    
