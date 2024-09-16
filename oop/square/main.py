from classes import Square

my_square = Square(4)

print(f"Current side: {my_square.get_side()}")
print(f"Area: {my_square.calculate_area()}")

my_square.change_side(6)
print(f"New side: {my_square.get_side()}")
print(f"New area: {my_square.calculate_area()}")
