 #do a program that asks which shift you study.
   #Ask to enter M-morning or V-Evening or N-Night. Print the message "Good Morning!", 
 #"Good Afternoon!" or "Good Night!" or "Invalid Value!", as applicable.."""

Shift = input("\n which shift do you study enter (M for morning, V for Evening, N for night)>>?").strip().lower()
    
if Shift == "m":
  print("Good morning ! ")

elif Shift == "v":
  print("Good Evening !")

elif Shift == "n":
  print("Good night !")
  

else :
  print("Invalid !")