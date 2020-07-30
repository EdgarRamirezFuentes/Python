## Son parecidos a los maps de c++, están conformados por un key y un value
diccionario = {
    "IDE" : "Integrated Development Enviroment",
    "OOP" : "Object Orientated Programming",
    "DBMS" : "Database Management System"
}

## Longitud de un diccionario
print(len(diccionario))

## Accediendo al valor de un elemento del diccionario
print(diccionario["OOP"])
print(diccionario.get("IDE")) ## Esta es otra forma de acceder al valor de una key

## Modificar el valor de una key de un diccionario
diccionario["OOP"] = "Object orientated programming"
print(diccionario.get("OOP"))

## Iterar los elementos de un diccionario con un ciclo for
for llave in diccionario: ## Itera en cada llave del diccionario
    print(llave, end="-")
    print(diccionario[llave])

for valor in diccionario.values(): ## Itera sobre los valores que contiene el diccionario omitiendo las keys
    print(valor)

## Checar la existencia de un elemento de un diccionario
print("API" in diccionario) ## Retorna un bool

## Agregar elemento al diccionario
diccionario["API"] = "Aplication Programming Interface"

## Remover elemento del diccionario
diccionario.pop("API")

## Limpiar todos los elementos del diccionario
diccionario.clear()

## Eliminar por completo la variable
del diccionario
