class Producto:
    contadorProductos = 0
    def __init__(self, nombre, precio):
        Producto.contadorProductos += 1
        self.__idProducto = Producto.contadorProductos
        self.__nombre = nombre
        self.__precio = precio
    
    def getID(self):
        return self.__idProducto
    
    def getNombre(self):
        return self.__nombre
    
    def getPrecio(self):
        return self.__precio
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setPrecio(self, precio):
        self.__precio = precio
        
    def __str__(self):
        return "ID: " + str(self.__idProducto) + " Nombre: " + self.__nombre + " Precio: " + str(self.__precio)