class Persona:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # setters
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre  

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido  
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad  


    # Metodo destructor
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

    # =========================
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido}, edad: {self._edad}')


if __name__ == '__main__':
    
    persona1 = Persona('Bettina', 'Rybicki', 61)
    persona1.nombre = 'Bettina Andrea'
    persona1.mostrar_detalle()