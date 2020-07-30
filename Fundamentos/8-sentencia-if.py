numero = int(input("Ingresa un número: "))
if numero%2==0:
    print("El número ingresado es par")
## Se puede utilizar la sentencia elif, que es mejor conocida como else if
else:
    print("El número ingresado es impar")
    
## También se puede utilizar el operador ternario
print("El número ingresado es par") if numero %2 == 0 else print("El número ingresado es impar")