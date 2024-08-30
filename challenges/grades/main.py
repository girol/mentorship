"""Write a program that reads the two partial grades obtained by a student in a subject over 
the course of a semester, and calculates their average. 
The assignment of grades follows the table below:"""


def print_line(delimiter="*"):
   print(delimiter * 70)
grade = float(input("\nEnter the mark for first Subject>>>>:"))
grade1 = float(input("\nEnter the mark for the second Subject>>>:"))
grade2 = float(input("\nEnter the mark for the third Subject>>>:"))
grade3 = float(input("\nEnter the mark for th fourt  Subject>>>:"))
grade4 = float(input("\nEnter the mark for the fifth Subject>>>:"))
average = (grade + grade1+ grade2 + grade3 + grade4)/5
print_line(delimiter="*")
print("               Sub1    Sub2       Sub3     Sub4     sub5    T-av Grade \n")

if 9 <= average <= 10 :
    print(f" the mark is:  {grade}     {grade1}      {grade2}      {grade3}    {grade4}    {average}     :A     ")
elif 7.5 <= average <= 9 :
    print(f" the mark is: {grade}      {grade1}       {grade2}      {grade3}    {grade4}    {average}      :B    ")
elif 6<= average <=7.5 :
    print(f" the mark is:  {grade}      {grade1}      {grade2}       {grade3}     {grade4}    {average}    :c     ")
elif 4 <= average <=6 :
    print(f" the mark is:  {grade}      {grade1}       {grade2}       {grade3}    {grade4}     {average}      :D     ")
elif 0 <= average <=4 :
    print(f" the mark is: {grade}        {grade1}       {grade2}       {grade3}     {grade4}   {average}      :Zero     ")
else:
    print(" the maximum mark is 10 you entered invalid number")
print_line(delimiter="*")