"""
Create a program that asks which shift you study.
Ask to enter one of:
 M - morning
 V - Evening
 N - Night.

Print the message:
"Good Morning!", "Good Afternoon!" or "Good Night!"
or "Invalid Value!", as applicable.
"""

shift = (
    input(
        "Which shift do you study enter (M for morning, V for Evening, N for night)? \n>> "
    )
    .strip()
    .upper()
)

if shift == "M":
    print("Good morning!")

elif shift == "V":
    print("Good Evening!")

elif shift == "N":
    print("Good night!")


else:
    print("Invalid !")
