
class Orden:
    contadorOrdenes = 0
    def __init__(self, productos):
        Orden.contadorOrdenes += 1
        self.__idOrden = Orden.contadorOrdenes
        self.__productos = productos
        
    def getID(self):
        return self.__idOrden
    
    def getProductos(self):
        productos = ""
        for producto in self.__productos:
            productos += producto.__str__() + "\n"
        return productos
    
    def agregarProducto(self, producto):
        self.__productos.append(producto)
        
    def getTotal (self):
        total = 0
        for producto in self.__productos:
            total += producto.getPrecio()
        return total
    
    def __str__(self):
        return "Orden: " + str(self.__idOrden) + "\n" + "Productos: \n" + self.getProductos()