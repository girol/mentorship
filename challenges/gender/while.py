# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

# Versão melhorada utilizando as técnicas:
#
# - While Loops
# - Constantes
# - Operador `in`

INPUT_MESSAGE = "type a letter:\n>>> "
VALID_GENDERS = ["M", "m", "F", "f"]

gender = input(INPUT_MESSAGE)

while gender not in VALID_GENDERS:
    print("Invalid input. Try typing 'F' or 'M' \n")
    gender = input(INPUT_MESSAGE)

if gender == "F":
    print("the person is female")

elif gender.upper() == "M":
    print("the person is male")
