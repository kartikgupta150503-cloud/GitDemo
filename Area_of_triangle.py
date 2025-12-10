"""
When all the length of the sides of the triangle is known - a, b, c

Semi perimeter (s) = (a + b + c)/2
Area = (s * (s-a) * (s-b) * (s-c))^0.5


a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

s = (a + b + c)/2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5

print("The area of the triangle is: ", round(area,2))
"""

"""

Area of a right angled triangle when the height and base is given by

Area = 0.5 * base * height

"""

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area2 = 0.5 * base * height

print("The area of the triangle is:", round(area2,2))
