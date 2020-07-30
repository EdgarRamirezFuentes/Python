## No es necesario asignar el tipo de una variable, solo se declara y se asigna el valor deseado.
x = 3
## Imprime el valor de la variable x
print(x)
## Cambiamos el valor de la variable
x = 8
## Vemos el cambio del valor de la variable
print(x)
## Cremos una nueva variable
y = 4
## Creamos una nueva variable y guardamos el resultado de la suma de x + y
z = x + y 
## Imprimimos el valor de la suma de x+y 
print(z)
## Hacer esto hace que la nueva variable creada apunte a la dirección de memoria de la variable asignada
a = z
## Verificamos que tengan el mismo valor
print(a)

## En teoría si cambio el valor de z, el valor de a también se verá modificado
z = 9
print(z)
print(a)
 ## Corriendo el código lanza que a = 12, por lo tanto no se ve la refencia de variables ya que si a estuviera 
 ## estuviera referenciando a z, a tendría como valor 9.


## Esta función muestra la posición en RAM de la variable deseada.
id(w)