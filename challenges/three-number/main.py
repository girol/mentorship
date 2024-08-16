#  Faça um Programa que leia três números e mostre o maior deles
a = input("Please enter the firs number    ")
b = input("please enter the second number   ")
c = input("please enter the third number    ")
if a >= b and a >= c :
    print(a)
elif b >= a and b >= c :
    print(b)
else:
   print(c)