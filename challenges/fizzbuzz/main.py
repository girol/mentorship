"""
Escreva um programa em Python que que conte de 1 a 100. Porém, se o número da vez for
divisível por 3, imprimir na tela a palavra "Fizz". Se for divisível por 5,
imprimir "Buzz" e se for divisível tanto por 3 quanto por 5, imprimir "FizzBuzz"
"""

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
