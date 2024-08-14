#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.




alpha = input("type a letter here")

if (alpha == 'a'or alpha == 'e'or alpha == 'i'or alpha =='o' or alpha == 'u'):
    print("the letter you typed is vowel")

elif (alpha == "w" or alpha == "y"):
    print("the letter you typed is semi vowel")

else:
    print("the letter you typed is consonant")
    