class Cubo:
    
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo



if __name__ == '__main__':
    
    ancho = int(input('Proporciona el ancho: '))
    alto = int(input('Proporciona el alto: '))
    profundo = int(input('Proporciona lo profundo: '))

    cubo1 = Cubo(ancho, alto, profundo)
    print(f'Volumen del Cubo: {cubo1.calcular_volumen()}')