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
        return self.side**2
