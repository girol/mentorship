# Faça um Programa que peça dois números e imprima o maior deles.

number1 = input("Please enter the first number: ")
number2 = input("Please enter the second number: ")

if number1 == number2:
    print("The numbers are the same")
elif number1 > number2:
    print(number1)
else:
    print(number2)
