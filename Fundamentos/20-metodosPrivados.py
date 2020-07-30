class Persona:
    def __init__(self, nombre, nacionalidad, edad):
        self.nombre = nombre ## Públuico
        self._nacionalidad = nacionalidad ## Protegido
        self.__edad = edad ## Privado
    
    ## Getters
    
    def getEdad(self):
        return self.__edad
    
    ## Setters
    
    def setEdad(self,edad):
        self.__edad = edad
        
    ## Methods        
    
    def metodoPublico(self):
        self.__metodoPrivado()
    
    def __metodoPrivado(self):
        print(self.nombre)
        print(self.nacionalidad)
        print(self.edad)