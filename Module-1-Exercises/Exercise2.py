import math
# Name input
user = input("Enter your name: ")
print(f"Nice to meet you, {user}!")

# Circle radius
r = float(input("Enter the radius of the circle : "))
print(f"The radius of the circle is {r}")
area = r * r * math.pi
print(f"The area of the circle is {area}")

# Rectangle perimeter & area
length =  float(input("Enter the length of the rectangle "))
width = float(input("Enter the width of the rectangle "))
perimeter = 2 * length + 2 * width
rectanglearea = length * width
print(f"The perimeter of the rectangle is {perimeter}")
print(f"The area of the rectangle is {rectanglearea}")

# Sum, Area and Average of three integers
first = int(input(f"Enter the first integer "))
second = int(input(f"Enter the second integer "))
third = int(input(f"Enter the third integer "))
integersum = first + second + third
integerproduct = first * second * third
integeraverage = (first + second + third) / 3
print(f"The sum of the integers is = {integersum}")
print(f"The product of the integers is = {integerproduct}")
print(f"The average of the integers is = {integeraverage}")

# Medieval unit conversion