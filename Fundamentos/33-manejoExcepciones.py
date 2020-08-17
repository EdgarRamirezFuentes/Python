
## * Implementación de una exception creada por nosotros.
from myExceptions.sameNumber import SameNumberException

a = None
b = None
resultado = None
try:
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    if(a == b):
        raise SameNumberException("Números idénticos") ## * Raise lanza la exception implementada
    resultado = a /b
    ''' * 
        Si ocurre un error al intentar la operación dentro del bloque try, se ejecutará la 
        operación dentro del bloque except para evitar detener la ejecución del programa.
    '''
except ValueError as e:
    print("Ocurrió un error", e)
    print(type(e)) ## * Sirve para conocer el tipo de exception
except ZeroDivisionError as e: 
    print("Ocurrió un error", e)
    print(type(e)) ## * Sirve para conocer el tipo de exception
except TypeError as e:
    print("Ocurrió un error", e)
    print(type(e)) ## * Sirve para conocer el tipo de exception
except Exception as e: ## * Sirve para manejar excepciones de manera genérica
    print("Ocurrió un error", e)
    print(type(e)) ## * Sirve para conocer el tipo de exception
else: ## * Se ejecuta cuando no hubo ninguna excepción en la ejecución (opcional)
    print("No ocurrió ninguna excepción")
finally: ## * Sin importar si hubo o no excepción, se va a ejecutar este bloque
    print("Finally")
    
print("Resultado:", resultado)
