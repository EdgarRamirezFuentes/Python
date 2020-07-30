## El encapsulamiento es evitar que se accedan a los atributos de nuestras clases de manera externa
class Persona:
    
    ## Constructor
    def __init__(self, nombre):
        self.__nombre = nombre ## Para asignar un atributo como privado, se agrega doble guión bajo.
    
    ## Getters
    def getNombre(self):
        return self.__nombre
    
    ## Setters
    def setNombre(self, nombre):
        self.__nombre = nombre

persona = Persona("Edgar")
print(persona.getNombre())
persona.setNombre("Alejandro")
print(persona.getNombre())