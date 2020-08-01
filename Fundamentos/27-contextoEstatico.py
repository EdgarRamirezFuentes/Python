class MiClase:
    ## * Se puede acceder a ella sin la necesidad de crear una instancia
    variableDeClase = "Variable de clase"
    
    def __init__(self, variableDeInstancia):
        ## * Únicamente se puede acceder a ella mediante una instancia de la clase.
        self.variableDeInstancia = variableDeInstancia
    
    ## * Este decorador declara que el siguiente método será de tipo static.
    ## * Se permite acceder a este método sin la necesidad de una instancia de la clase.
    ## * No pueden acceder a las variables de instancia.
    @staticmethod
    def metodoStatic():
        print("Accediendo al método static") 
        ## * Si se quiere acceder a una variable de clase, se hace de esta manera.
        print(MiClase.variableDeClase)
    
    
    ## * Este decorador declara que el siguiente método será de tipo clase.
    ## * Recibe como parámetro una clase y se puede acceder a él sin la necesidad de una instancia.
    ## * No pueden acceder a las variables de instancia.
    @classmethod
    def metodoClase(cls):
        print("Accediendo al método de clase de la clase ", str(cls))
        ## * Si se quiere acceder a una variable de clase, se hace de la siguiente manera.
        print(cls.variableDeClase)
    
    ## * Se puede acceder a los métodos de clase y static desde un método de instancia.
    ## * Se necesita de una instancia de la clase para poder utilizar este método.
    def metodoDeInstancia(self):
        self.metodoStatic()
        self.metodoClase()
        
objeto1 = MiClase("Variable de instancia")

## * Una instancia puede acceder tanto a las variables de instancia, como a las variables de clase
print(objeto1.variableDeInstancia)
print(objeto1.variableDeClase)

## * Al ser una variable de clase se puede acceder a ella sin la necesidad de crear una instancia
print(MiClase.variableDeClase)

## ! Tira error porque no se puede accerder a una variable de instancia dese la clase
## ! print(MiClase.variableDeInstancia)

## * Al ser un método static, se puede acceder a él sin la necesidad de una instancia de la clase
MiClase.metodoStatic()

## * De igual manera una instancia de la clase puede acceder a este tipo de métodos
objeto1.metodoStatic()

## * Al ser método de calse, se puede acceder a él sin la necesidad de una instancia de la clase
MiClase.metodoClase() 

## * De igual manera se puede acceder a este por medio de una instancia
objeto1.metodoClase()

## * Accediendo a los métodos static y de clase desde el método de instancia
objeto1.metodoDeInstancia()

## ! No se puede acceder a este método porque se necesita tener una instancia de la clase para poder hacer uso de este.
## ! MiClase.metodoDeInstancia()