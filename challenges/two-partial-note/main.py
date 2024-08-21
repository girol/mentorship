

def print_line(delimeter="*"):
    print(delimeter *40)
print("The partial notes and average grade of student that shows student qualification:\n Grade number is from  1 to 10")



print_line()
note1 = float(input("Please enter the first partial grade>>>"))
note2 = float(input("Please enter the second partial grade>>>" ))
print_line()
average = (note1+note2) / 2
if average == 10 :
    print("Passed with distinction",average)
elif average >=7:
    print("Approved",average)
else:
    print("failed",average)

print_line()
    