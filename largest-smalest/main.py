#Faça um Programa que leia três números e mostre o maior e o menor deles


list = []
num =  int(input("enter the range numbers: "))
for i in range(1, num + 1):
    ele = int(input("enter numbers"))
    list.append(ele)
print("largest number is ", max(list))
print("Smallest numbe is ", min(list))