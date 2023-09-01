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
weight_in_talents = float(input("Give the weight in talents: "))
weight_in_pounds = float(input("Give the weight in pounds: "))
weight_in_lots = float(input("Give the weight in lots: "))
talents_in_kilograms = weight_in_talents * 8.512
pounds_in_kilograms = weight_in_pounds * 0.4256
lots_in_kilograms = weight_in_lots * 0.0133
total_weight_in_kg = int(talents_in_kilograms + pounds_in_kilograms + lots_in_kilograms)
total_weight_in_grams = (talents_in_kilograms + pounds_in_kilograms + lots_in_kilograms) %1*1000
print(f"The weight in modern units is {total_weight_in_kg} kilograms and {total_weight_in_grams} grams.")

# Code generator for code locks
import random
code3 = random.randint(1, 10**3)
code3gen = '{:03}'.format(code3)
code4 = random.randint(1, 10**4)
code4gen = '{:04}'.format(code4)

answer = int(input("How long of a code would you like to generate? 3 or 4? = "))
if answer == 3:
    print(f"Your 3 digit code is {code3gen}")
elif answer == 4:
    print(f"Your 4 digit code is {code4gen}")
else:
    print("Please enter 3 or 4.")