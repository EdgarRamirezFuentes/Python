from classes.InputDevice import InputDevice


class Mouse(InputDevice):
    quantity = 0

    def __init__(self, name, brand, price):
        super().__init__(name, price, brand)
        Mouse.quantity += 1
        self.__id = Mouse.quantity

    def getID(self):
        return self.__id

    def __str__(self):
        return (
            f"Mouse:\n"
            f"ID: {str(self.getID())}\n"
            f"Name: {super().getName()}\n"
            f"Brand: {super().getBrand()}\n"
            f"Price: ${super().getPrice()}\n"
        )
