class Persona:
    
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, edad {self.edad} {self.valores} {self.terminos}')



persona1 = Persona('Juan', 'Perez', 28,)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Juarez'
persona1.edad = 25
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido}, edad {persona1.edad} ')

persona2 = Persona('Karla', 'Gomez', 30)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido}, edad {persona2.edad} ')

persona3 = Persona('Nahir', 'Labudia', 26, '465456465', 2, 3, 5, m='manzana', p='pera')
persona3.mostrar_detalle()