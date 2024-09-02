

"""Write a program that reads the two partial grades obtained by a student in a subject over 
the course of a semester, and calculates their average. 
The assignment of grades follows the table below:"""


def calculate_grade(grade1, grade2):
    grade = grade1 + grade2 /2
def print_line(delimiter="*"):
    print(delimiter * 50)
print_line("*")
grade1 = float(input("\nPlease enter the first grade from zero to ten>>:"))
grade2 = float(input("\nPlease enter the second grade  from zero to ten>>:"))
average = (grade1 + grade2) /2

if 9 <= average  <= 10 :
        grade = "A"
elif 7.5 <= average < 9 :
         grade = "B"
elif 6<= average < 7.5 :
        grade = "C"
elif 4 <= average < 6 :
        grade ="D"
elif 0 <= average < 4 :
        grade = "Zero"
else:
    print("you enter invalid number")

calculate_grade(grade1,grade2)

print(f"\nThe average grade is : {average}" )
print(f"\nthe letter_grade is:{grade:}")
print_line("*")

