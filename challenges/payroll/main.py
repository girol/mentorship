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


worked_hours = float(input("Please enter the number of hours you worked this month: "))
hour_payment = float(input("Please enter hour payment: "))

gross_salary = hour_payment * worked_hours

if gross_salary <= 900:
    irs = 0
elif gross_salary <= 1500:
    irs = 5
elif gross_salary <= 2500:
    irs = 10
else:
    irs = 20

irs = irs / 100
FGTS = 11 / 100
union = 3 / 100
retirement = 10 / 100

if irs > 0:
    ir_deduction = gross_salary * irs
else:
    ir_deduction = 0


retirement_deduction = gross_salary * retirement
fgts_bonus = gross_salary * FGTS
net_salary = gross_salary - retirement_deduction - ir_deduction
print_line(delimiter="=")

print(
    f"""
    Gross Salary: {worked_hours} * {hour_payment} : {gross_salary}
        Deductions:
        (-) IR: {irs * 100}% = {ir_deduction}
        (-) INSS: 10% = {retirement_deduction}
    FGTS (11%) = {fgts_bonus}
"""
)

print_line(delimiter="-")
print(
    f"""
    Total Discount: {retirement_deduction + ir_deduction}
    Net Salary: {net_salary}
"""
)
