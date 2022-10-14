from Persona2 import Persona

if __name__ == '__main__':

    print('Creacion objetos'.center(50,'-'))
    persona1 = Persona('Karla', 'Gomez', 30)
    persona1.mostrar_detalle()

    print('Eliminacion objetos'.center(50,'-'))
    del persona1