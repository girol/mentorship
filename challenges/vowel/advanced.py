## This is an advanced solution using Exceptions
import sys

VOWELS = ["a", "e", "i", "o", "u"]
alpha = input("type a letter: ")

if len(alpha) > 1:
    sys.exit("Invalid input: Type just one character")

def check_character(character):
    if character in VOWELS:
        print("the letter you typed is vowel")
    else:
        print("the letter you typed is consonant")

try:
    int(alpha)
except ValueError:
    check_character(alpha)
else:
    sys.exit(f"Invalid input: {alpha} is a number")