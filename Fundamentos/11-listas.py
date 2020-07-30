## Las listas son parecidas a los arrays
nombres = ["Edgar", "Yael", "Jair", "Iván", "Tony"]

## Esta función muestra el tamaño de una lista
print(len(nombres))

## Para acceder a un elemento de una lista, lo haríamos de la siguiente manera
print(nombres[0])

## En python también se puede acceder a elementos de una lista de forma inversa
print(nombres[-1]) ## Retorna el último elemento de una lista

## También podemos obtener los elementos de una lista por rango
print(nombres[0:3]) ## El primer valor es desde donde va a comenzar a "contar" y el segundo es donde terminará de contar (No lo toma en cuenta)

## Otra forma para pedir información desde el inicio de las lista hasta el índice propocionado, sería de la siguiente forma
print(nombres[:4]) ## Omitir el primer índice hace referencia que se iniciará desde el índice 0
 
## Se puede hacer lo mismo con el índice final
print(nombres[1:]) ## Omitir el segundo índice hace referencia a que se terminará hsata el último elemento de la lista

## Omitir ambos índices hace referencia a todos los elementos del array
print(nombres[:])

## Se pueden iterar los elementos de la lista con un for de la siguiente manera
for nombre in nombres:
    print(nombre)
    
## Revisar que existe un elemento en una lista
print("Edgar existe en la lista") if "Edgar" in nombres else print("Edgar existe en la lista")

## Agregar nuevo en la lista en la parte de atrás(push back)
nombres.append("Hector")

## Agregar en el índice propocionado

nombres.insert(1,"Rodolfo")

## Eliminar un elemento de la lista
nombres.remove("Hector")

## Remover el último elemento de la lista
nombres.pop()

## Remover el elemento en el índice indicado
del nombres[3]

## Limpiar los elementos de nuestra lista
nombres.clear()

## Eliminar la lista de memoria
del nombres


    