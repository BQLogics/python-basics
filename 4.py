#swap 2 variable 

num1 = float(input("enter a number to swap:"))
num2 = float(input("enter another number:"))

a=num1
b=num2

print(f"before swap your numbers are \na = {num1} \nb = {num2}")

#swap logic

temp=a
a=b
b=temp

print(f"after swapping the numbers num1 is \na = {a}\nb= {b}")

