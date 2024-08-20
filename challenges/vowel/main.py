#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.




alpha = input("type a letter here")

VOWELS = ["a", "e", "i", "o", "u"]

if alpha in VOWELS:
    print("the letter you typed is vowel")

else:
    print("the letter you typed is consonant")
 