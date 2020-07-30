## Así se solicita al usuario el ingreso de datos desde la consola
datoIngresado = input()

## Si se desea agregar un mensaje para el ingreso del dato, se manda como parámetro de la función
datoIngresado = input("Ingresa tu nombre: ")

## Los datos que recibe la función input son de tipo string, por lo tanto, no se pueden hacer ingreso de
## números enteros solo usando esta función 
numero1 = input() # 1
numero2 = input() # 2

print(numero1 + numero2) ## El resultado es 12

## Para recibir números enteros usando esta función, debemos hacer un casteo a tipo int de lo que reciba input
numero1 = int(input()) ## 1
numero2 = int(input()) ## 2
print(numero1 + numero2) ## El resultado es 3

