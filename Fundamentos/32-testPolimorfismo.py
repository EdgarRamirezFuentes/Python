from polimorfismo.Empleado import Empleado
from polimorfismo.Gerente import Gerente

def imprimirDetalles(objeto):
    print(objeto.__str__())
    
empleado = Empleado("Edgar", 35500.5)
imprimirDetalles(empleado)
gerente = Gerente("Alejandro", 45800.00, "Sistemas computacionales")
imprimirDetalles(gerente)