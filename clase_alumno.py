#1.Haz una clase fácil, como Alumno, con nombre y nota, con un método imprimir().
#2. Crea una instancia de Alumno, mostrando sus datos y llamando al método desde otro módulo

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir_info(self):
        print(f"El alumno {self.nombre} ha sacado la siguiente nota: {self.nota}")