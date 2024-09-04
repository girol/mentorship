"""Write a program that reads the two partial grades obtained by a student in a subject over
the course of a semester, and calculates their average.
The assignment of grades follows the table below:"""


def calculate_average(grade1, grade2):
    average = (grade1 + grade2) / 2
    return average

def calculate_concept(average):
    if 9 <= average <= 10:
        concept = "A"
    elif 7.5 <= average < 9:
        concept = "B"
    elif 6 <= average < 7.5:
        concept = "C"
    elif 4 <= average < 6:
        concept = "D"
    else:
        concept = "E"
    return concept

def print_line(delimiter="*"):
    print(delimiter * 50)


def run():
    print_line("*")

    grade1 = float(input("\nPlease enter the first grade from 0 to 10 >>: "))
    grade2 = float(input("\nPlease enter the second grade from 0 to 10 >>: "))

    average = calculate_average(grade1, grade2)
    concept = calculate_concept(average)

    print(f"\nThe average is: {average}")
    print(f"\nthe concept is: {concept}")
    print_line("*")
    print(f"\n RESULT: \n")

    if concept in ["A", "B", "C"]:
        print("APPROVED! :) ")
    else:
        print("FAILED :(")

if __name__ == "__main__":
    run()