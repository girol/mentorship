#  Faça um Programa que leia três números e mostre o maior deles

print("Please, input 3 numbers\n")

number_list = []

for i in range(1, 4):

    number = input(f"Input the {i}° number: ")
    number_list.append(int(number))

number_list.sort()

highest = number_list[2]

print(f"The highest number is: {highest} ")
