## A diferencia de las lista, las tuplas también mantienen el orden en el que fueron agregaados, pero no se puede modificar
frutas = ("Manzana", "Pera", "Mango", "Guayaba")

## Para conocer el tamaño de la tupla utilizamos la siguiente función
print(len(frutas))

## Acceder a un elemento  de la tupla
print(frutas[0])

## También existe la navegación inversa.
print(frutas[-1]) ## Imprime el último elemento

## Acceder por rango
print(frutas[1:3])

## No es posible modificar los elementos ya ingresados en la tupla.
## Lo que se podría hacer para modificar los datos de una tupla, sería hacer un casteo a una lista y una vez
## modificado, convertimos esa lista en una tupla
print(frutas)
frutasLista = list(frutas)
frutasLista[0] = "Fresa"
frutas = tuple(frutasLista)
print(frutas)

## Se puede iterar una tupla con un ciclo for
for fruta in frutas:
    print(fruta, end =" ") ## El parámetro end indica el caracter que se agregará al final de la impresión, por defecto está el salto de línea
    
## Para eliminar por completo la tupla usamos la siguiente función
del frutas
