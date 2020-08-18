from classes.Monitor import Monitor
from classes.Keyboard import Keyboard
from classes.Mouse import Mouse
from classes.Computer import Computer
from classes.Order import Order

order = Order()

keyboard = Keyboard("KGB 500", "GameFactor", 50)
mouse = Mouse("G300S", "Logitech", 25)
monitor = Monitor("Monitor", "HP", 100, "15.7")
computer = Computer("Pavilion 15", monitor, mouse, keyboard, 300)

keyboard2 = Keyboard("KGB 500", "GameFactor", 50)
mouse2 = Mouse("G300S", "Logitech", 25)
monitor2 = Monitor("Monitor", "HP", 100, "15.7")
computer2 = Computer("Pavilion 15", monitor2, mouse2, keyboard2, 300)

order.addProduct(computer)
order.addProduct(computer2)

## order.deleteProduct(1)
print(order)