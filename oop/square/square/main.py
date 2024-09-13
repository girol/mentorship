from classes import Square
my_square = Square (4)

print(f"current side:{my_square.get_side()}")

print(f"Area:{my_square.calculate_area()}")

Square.change_side(6)
print(f"new side :{my_square.get_side()}")
print(f"new area:{my_square.calculate_area()}")
