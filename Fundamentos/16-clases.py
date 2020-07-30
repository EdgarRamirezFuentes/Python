## Para crear una clase se utiliza la palabra reservada class
class Persona: 
    ## Constructor
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad     
        
## Creando una instancia de la clase persona
persona = Persona("Edgar", 21)

## Accediendo a los valores de la instancia
print(persona.nombre)
print(persona.edad)


class Aritmetica:
    
    ## Constructor
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    ## Métodos
    def suma(self):
         return self.operando1 + self.operando2
     
    def resta(self):
        return self.operando1 - self.operando2
    
    def multiplicacion(self):
        return self.operando1 * self.operando2
    
    def division(self):
        return self.operando1 / self.operando2

aritmetica = Aritmetica(2,3)
print(aritmetica.suma())
print(aritmetica.resta())
print(aritmetica.multiplicacion())
print(aritmetica.division())

class Alumno:
    ## Constructor
    def __init__(self, boleta, nombre, *materias): ## El asterístco significa que el valor es opcional y armará una tupla con los argumentos sobrantes.
        self.boleta = boleta
        self.nombre = nombre
        self. materias = materias
        
    ## Methods
    
    def printData(self):
        print("Boleta: ", self.boleta)
        print("Nombre: ", self.nombre)
        print("Materias: ", self.materias)
        
alumno = Alumno("2014131046", "Edgar Ramírez", "Tecnología web", "Matemáticas avanzadas para la ingeniería", "Redes de computadoras", "Administación financiera")
alumno.printData()      

class Profesor: 
    
    ## Constructor
    
    def __init__(self, clave, nombre, **materias): ## El doble * indica que se le mandará un diccionario como argumento y es un parámetro opcional
        self.clave = clave
        self.nombre = nombre
        self. materias = materias
        
    ## Methods
    
    def printData(self):
        print("Clave: ", self.clave)
        print("Nombre: ", self.nombre)
        print("Materias: ", self.materias)

profesor = Profesor("2014131046", "Edgar Ramírez", TB = "Tecnologías web", MAPI = "Matemáticas avanzadas para la ingeniería", AF = "Administación financiera")
profesor.printData()