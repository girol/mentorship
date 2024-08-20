import sys

VOWELS = ["a", "e", "i", "o", "u"]
NUMBERS = ["1", "2", "3", "4", "5", "6", "8", "9", "0"]

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
alpha = input("type a letter: ")

if len(alpha) > 1:
    sys.exit("Invalid input: Type just one character")

if alpha in NUMBERS:
    sys.exit(f"Invalid input: {alpha} is a number")

if alpha in VOWELS:
    print("the letter you typed is vowel")

else:
    print("the letter you typed is consonant")
