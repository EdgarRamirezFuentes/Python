from classes.InputDevice import InputDevice


class Keyboard(InputDevice):
    quantity = 0

    def __init__(self, name, brand, price):
        super().__init__(name, price, brand)
        Keyboard.quantity += 1
        self.__id = Keyboard.quantity

    def getID(self):
        return self.__id

    def __str__(self):
        return (
            f"Keyboard: \n"
            f"ID: {str(self.getID())}\n"
            f"Name: {super().getName()}\n"
            f"Brand: {super().getBrand()}\n"
            f"Price: ${super().getPrice()}\n"
        )
