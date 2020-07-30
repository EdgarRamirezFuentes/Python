## Una colección de tipo set no mantienen orden y sus elementos son únicos y no modificables.
## Se pueden agregar y eliminar elementos
planetas = {"Marte", "Júpiter", "Venus"}
print(planetas)

## Conocer la longitud de un set
print(len(planetas))

## Buscar un elemento dentro de nuetro set
print("Tierra" in planetas)

## Agregar nuevos elementos al set
planetas.add("Mercurio")

## Si queremos agregar el mismo elemento al set, no se agregará porque ya existe un registro de ese elemento
planetas.add("Mercurio")

## Para eliminar tenemos dos métodos
planetas.remove("Mercurio") ## Arroja una exception en caso de que el elemento no exista.
planetas.discard("Tierra") ## No arroja exception en caso de que el elemento no exista en el set

## Limpiar el set completamente
planetas.clear()

## Eliminar completamente la variable
del planetas

