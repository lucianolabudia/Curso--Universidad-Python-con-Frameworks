class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura



if __name__ == '__main__':
    
    base = int(input('Proporciona la base: '))
    altura = int(input('Proporciona la altura: '))

    rectangulo1 = Rectangulo(base, altura)
    print(f'Area rectangulo: {rectangulo1.calcular_area()}')

    base = int(input('Proporciona la base: '))
    altura = int(input('Proporciona la altura: '))

    rectangulo2 = Rectangulo(base, altura)
    print(f'Area rectangulo: {rectangulo2.calcular_area()}')