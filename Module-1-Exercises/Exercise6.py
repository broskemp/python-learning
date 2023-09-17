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
