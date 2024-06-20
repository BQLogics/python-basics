# 1.write hello python program
# 2.write program to do arithmetical operation addition and division
# 3.find the area of triangle
# 4.swap 2 variable
# 5.generate random number using random module
# 6.convert kilometers to  miles
# 7.convert celsius to fahrenhiet

''' 1.write hello python program
--------------------------------'''

print("hello python")


'''2.write addition program and division program
----------------------------------------------'''

num1 = float(input("enter any number: "))
num2 = float(input("enter any another number: "))
print("======================")
print("choose your operation")
print("======================")
print("1.Addition\n2.Division\n3.Area of Triangle\n4.Swap Number")
print("----------------------")

choice=int(input("your choice :"))


if choice == 1:
    print(f"{num1}+{num2} = ",num1+num2)
elif choice ==2:
                if(num2!=0):
                        print(f"{num1}/{num2} =",num1/num2)
                else:
                        print("oooh your diviser is zero please check it again by changing diviser")
elif choice ==3:
            print(f"{num1} is taken as base & {num2} is taken as height\nArea of triangle is =",0.5*num1*num2)    
elif choice ==4:
           print(f"before swaping \n num1={num1}\n num2={num2}")
           temp=num1
           num1 = num2
           num2 = temp 
           print(f"ater swaping \n num1={num1} \n num2={num2}")
else:
        print("oooh no ! check your choice")
            
                

    
    