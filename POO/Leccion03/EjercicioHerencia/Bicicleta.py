from Vehiculo import *

class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()}, Tipo: {self.tipo}'


if __name__ == '__main__':

    bicicleta = Bicicleta('Verde', 2, 'urbana')
    print(bicicleta)