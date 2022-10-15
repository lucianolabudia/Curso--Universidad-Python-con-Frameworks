from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


if __name__ == '__main__':

    print('Creacion Objeto Cuadrado'.center(50,'-'))
    cuadrado1 = Cuadrado(5, 'Rojo')
    print(cuadrado1.ancho)
    print(cuadrado1.alto)
    print(cuadrado1.color)
    print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
    print(cuadrado1)

    # MRO - Method Resolution Order
    # print(Cuadrado.mro())    

    print('Creacion Objeto Rectangulo'.center(50,'-'))
    rectangulo1 = Rectangulo(3, 8, 'Verde')
    print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
    print(rectangulo1)

