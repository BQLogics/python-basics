import cmath

# Get coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = cmath.sqrt(b**2 - 4*a*c)

# Calculate the two roots
root1 = (-b + discriminant) / (2*a)
root2 = (-b - discriminant) / (2*a)

# Display the roots
print(f"The roots of the quadratic equation are {root1} and {root2}")
