class Order:
    quantity = 0

    def __init__(self):
        Order.quantity += 1
        self.__id = Order.quantity
        self.__products = {}

    def getID(self):
        return self.__id

    def addProduct(self, product):
        self.__products[str(product.getID())] = product

    def getProducts(self):
        return self.__products
    
    def listProducts(self):
        products = ""
        for product in self.__products.values():
            products += product.__str__()
            products += "\n\n------------------------------------------\n\n"
        return products
    
    def getTotal(self):
        total = 0
        for product in self.__products.values():
            total += product.getTotal()
        return total
    
    def deleteProduct(self, id):
        self.__products.pop(str(id))

    def __str__(self):
        return (
            f"ID order: {str(self.getID())}\n"
            f"Products:\n"
            f"-----------------------------------\n"
            f"{self.listProducts()}"
            f"\n\n-----------------------------------\n\n"
            f"Total (Order): ${str(self.getTotal())}"
        )
