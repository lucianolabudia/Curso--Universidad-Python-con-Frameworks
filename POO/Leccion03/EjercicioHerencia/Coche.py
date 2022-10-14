from Vehiculo import *

class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}, Velocidad: {self.velocidad}km/hr'


if __name__ == '__main__':

    coche = Coche('Rojo', 4, 100)
    print(coche)