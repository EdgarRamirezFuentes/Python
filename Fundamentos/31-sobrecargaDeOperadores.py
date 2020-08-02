
## *  El operador + es un ejemplo de la sobrecarga de operadores debido a que se comporta de diferentes 
## * formas dependiendo del tipo de datos con los que esté trabajando.

## * Suma 
a = 1
b = 2
print(a+b)

## * Concatena 
a = "Hola "
b = "mundo"

print(a+b)
 
## * Crea una lista que contiene a las dos listas
a = [1,2]
b = [3,4]

print(a+b)

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    ## * Esta sobrecarga hace posible que podamos usar el operador "+" en las clases personas.  
    def __add__(self, p2):
        self.__nombre += " " + p2.__nombre
        return self.__nombre
        

''' * 
    Nativamente la clase object no tiene algún método add que soporte como parámetros objetos de tipo
    Persona, pero gracias a la sobrecarga de operadores nosotros podemos sobreescribir este método
    en la clase Persona para que al llamar el método add, pueda hacer algo.
'''
p1 = Persona("Edgar")
p2 = Persona("Alejandror")
print(p1 + p2)