from disenioDeClases.Producto import  Producto
from disenioDeClases.Orden import Orden

producto1 = Producto("Camisa", 300)
producto2 = Producto("Sudadera", 800)
producto3 = Producto("Gorro", 250)
producto4 = Producto("Calcetines", 150)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
 
orden1 = Orden(productos1)
orden2 = Orden(productos2)

orden1.agregarProducto(producto3)
orden2.agregarProducto(producto1)

print(orden1)
print(orden2)

print("El precio total de la orden 1 es: ", orden1.getTotal())
print("El precio total de la orden 2 es: ", orden2.getTotal())
