"""Organizations decided to give their employees a salary increase and hired him to develop the
 program that will calculate the adjustments.
Create a program that receives an employee's salary and readjusts it according to the following criteria, 
based on the current salary:
salaries up to R$280.00 (including): 20% increase
salaries between R$280.00 and R$700.00: 15% increase
salaries between R$700.00 and R$1500.00: 10% increase
salaries from R$ 1500.00 onwards: 5% increase After the increase is made, inform on the screen:
the salary before the adjustment;
the percentage of increase applied;
the amount of the increase;
the new salary, after the increase."""

current_salary = float(input("Enter the amount of current salary <<>>:"))
def print_line(delimiter="*"):
    print(delimiter * 50)


if current_salary <= 280 :
    percentage_increase  = 20
elif current_salary <= 700:
    percentage_increase = 15
elif current_salary <= 1500 :
    percentage_increase = 10
else: 
    percentage_increase = 5

increase_amount = (percentage_increase/100)*current_salary
new_salary = current_salary + increase_amount
print_line(delimiter="*")
print(f"Salary before the adjustment:>>> {current_salary:.2f}\n")
print(f"Percentage of increase applied:>>> {percentage_increase}%\n")
print(f"Amount increased>>> {increase_amount}\n")
print(f"New salary after the adjustment:>>> {new_salary:.2f}\n")
print_line(delimiter="*")