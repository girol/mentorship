#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

value = float(input("please enter the number "))
if value > 0:
    print("the number is you entered is positive +")
elif value == 0:
    print("the number is 0")
else:
    print("the number you entered is negative -")