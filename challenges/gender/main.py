# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

cha = input("type a letter:\n>>> ")

if cha.upper() == "F":
    print("the person is female")

elif cha.upper() == "M":
    print("the person is male")

else:
    print("Invalid input. Try typing 'F' or 'M'")
