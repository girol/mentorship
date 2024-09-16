"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""

class Square:

    def __init__(self, side):
        self.side = side

    def change_side(self, new_side):
        self.side = new_side

    def get_side(self):
        return self.side 

    def calculate_area(self):
        return self.side **2

square = Square(4)
print(f"current side:{square.get_side()}")

print(f"Area:{square.calculate_area()}")

square.change_side(6)
print(f"new side :{square.get_side()}")
print(f"new area:{square.calculate_area()}")

