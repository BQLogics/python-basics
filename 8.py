# write a python program to check if a number is positive negative or zero

num=float(input("enter a number: "))

if num > 0:
    print ("the number is positive")

elif num == 0:
    print("ooops! its zero ")
else:
    print("{} is negative".format(num))