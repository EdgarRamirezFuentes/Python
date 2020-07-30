## Las funciones se declaran con la palabra reservada def

## Función sin parámetros y sin retorno
def MyFunction():
    print("Ejecutando mi función")
    
MyFunction()

## Función con parámetros y sin retorno
def saludo(nombre, apellido):
    print("Hola", nombre, apellido)
    
saludo("Edgar", "Ramírez")

## Funciones con parámetros y con retorno
def suma(a = 0,b = 0): ## Si no se le mandan argumentos a la función, tomará los valores pro default
    return a+b

print(suma())
print(suma(1,2))
