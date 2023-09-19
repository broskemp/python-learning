import random


# write a function that returns a random dice roll between 1 and 6
# write a main program that rolls the dice until the result is 6 (and prints every roll)
def rolldie(x):
    dice = random.randint(1, x)
    return dice


x = int(input("How many sides should your die have?: "))
while (a := rolldie(x)) < x:
    print(f"Dice rolled was {a}")
print(f"Dice roll of {a} has been achieved. Ending sequence.")


# gallons to liters conversion
def gallonconversion(g):
    gallontoliters = g * 3.78541
    return gallontoliters


gallons = float(input("How many gallons would you like to convert to liters?: "))
gallonconversion(gallons)
print(gallonconversion(gallons))

# function to get a list of integers, then returns the sum of all the numbers
# write a main program where you create a list, call the function and print the value


def listsum(intlist):
    numberlist = sum(intlist)
    return numberlist


def remove_odd(l):
    return [x for x in l if x % 2 == 0]


numbers = [1, 3, 5, 8, 10]
print(f"Here is a list of numbers : {numbers}")
listsum(numbers)
print(f"Here is the sum of the list of numbers : {listsum(numbers)}")
remove_odd(numbers)
print(f"Here is the list but with only even numbers : {remove_odd(numbers)}")


# write a function that receives two parameters : diameter of pizza in cm and price of pizza in eur
# the function calculates and returns the unit price of the pizza per square meter
# main program asks the user of the diameter and price of two pizzas, and says which one has more value

def pizzacalculator():
    pizzadiameter = int(input("Enter the diameter of pizza in cm : ")) * 3.14
    pizzaprice = float(input("Enter the price of pizza in euros : "))
    unitprice = pizzadiameter / pizzaprice
    return unitprice


print("Loading calculations for Pizza 1 ...")
Pizza1 = pizzacalculator()
print("Loading calculations for Pizza 2 ...")
Pizza2 = pizzacalculator()

if Pizza1 > Pizza2:
    print("Pizza 1 is a better deal than Pizza 2")
elif Pizza1 == Pizza2:
    print("Both pizzas are equally worth it")
else:
    print("Pizza 2 is a better deal than Pizza 1")
