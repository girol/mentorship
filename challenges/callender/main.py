"""
Make a Program that reads a number and displays the corresponding day of the week.
(1-Sunday, 2-Monday, etc.),
if you enter another value, an invalid value will appear.
"""

day_number = int(
    input("Enter a number from one two seven to get the corresponding day of the week: ")
)

days_of_week = {
    1: "sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Satruday",
}

if 1 <= day_number <= 7:
    print(
        f"The day corresponding to number {day_number} is {days_of_week[day_number]}."
    )
else:
    print("please enter a number between 1 and 7")
