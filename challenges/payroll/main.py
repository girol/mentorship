"""Create a program to calculate a payroll, knowing that the deductions are from Income Tax, 
which depends on the gross salary (as per the table below) and 3% for the Union and that the FGTS corresponds to 11% of
 the Gross Salary, but it is not discounted (it is the company that deposits it).
 Net Salary corresponds to Gross Salary minus discounts. The program should ask the user for their hourly rate
   and the number of hours worked in the month.
IR Discount:
Gross Salary up to 900 (inclusive) - exempt
Gross Salary up to 1500 (inclusive) - 5% discount
Gross Salary up to 2500 (inclusive) - 10% discount
Gross Salary above 2500 - 20% discount Print the information on the screen, arranged as per the example below. 
In the example, the hour value is 5 and the hour quantity is 220."""



def print_line(delimiter="*"):
   print(delimiter * 70)
hourly_rate = float(input("\n Please enter the number of hour you worked this month**"))
gross_salary  = float(input("please enter the gross salary**"))
if gross_salary <= 900:
    tax = 0
elif gross_salary <= 1500:
    tax = 5
elif gross_salary <= 2500:                  
    tax = 10
else:
   tax = 20

gross_salary = (gross_salary+5 * hourly_rate )
tax = (tax/100)
FGTS = (11/100)
union = (3/100)
total_deduction = (tax+FGTS+union)
Net_salary = (gross_salary - total_deduction)
print_line(delimiter="*")

print(f"\n The gross salary during this month is equal to======= *GROSS SALARY* {gross_salary}")
print(f"\n the total tax amount is for the salary and hour you worked ==*TOTAL TAX* {tax:.2f}")
print(f"\n the deduction of FGTS is equal to=== *FGTS* 11%  ======================== {FGTS:}")
print(f" \n the discount for the union is=== *UNION* 3% =========================== {union:}")
print(f" \n Total amount to be deducted from the gross salary is =====*Totalded* {total_deduction:.2f}")
print(f"\n the Net Salary after tax and discount is equal to=========*Net Salary* {Net_salary}")
print_line(delimiter="*")


