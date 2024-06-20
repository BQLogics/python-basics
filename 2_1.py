#write a program to divide a number

num1= float(input("enter any number :"))
num2= float(input("enter any second number:"))

divi= num1-num2

print(f"your numbers are {num1}-{num2}={divi}")
print("your number are %s + %s = %s"%(num1,num2,divi))


# division

num1 = float(input("enter a number: "))
num2 = float(input("enter another number: "))

if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    divi = num1/ num2
    print(f" division of the {num1}/{num2}={divi}")
