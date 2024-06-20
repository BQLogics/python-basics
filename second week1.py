import calendar

year = int(input("enter year: "))
month = int(input("enter month: "))
date = int(input("enter date: "))

cal = calendar.month(year, month , date)

print(cal)