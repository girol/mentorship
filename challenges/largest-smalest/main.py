# Faça um Programa que leia três números e mostre o maior e o menor deles

numbers = []


def print_line(delimiter="="):
    print(delimiter * 22)


print_line(delimiter="#")
print("Calculates the max and min number")
print_line(delimiter="#")


for i in range(1, 4):

    number = input(f"Input the {i}° number: ")
    numbers.append(int(number))

print_line()
print("largest number is: ", max(numbers))
print("Smallest numbe is: ", min(numbers))
print_line()
