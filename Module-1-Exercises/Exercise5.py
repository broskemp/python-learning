import random

# problem 6) from exercise set 4 first

interval = int(input("Please enter a number of points to generate an estimation of pi : "))
circle_points = 0
square_points = 0

for i in range(interval**2):
    # randomly generated x and y values in an uniform way
    rand_x = random.uniform(-1,1)
    rand_y = random.uniform(-1,1)
    # distance between x, y from the origin point 0,0
    origin_dist = rand_x**2 + rand_y**2
    # checking if x, y lies inside the circle
    if origin_dist <= 1:
        circle_points += 1

    square_points += 1

    # estimating value of pi with this info
    # pi = 4 * number of points generated INSIDE the circle / points inside the SQUARE
    pi = 4 * circle_points / square_points

print(f"Final approximation of pi = {pi}")

# write a program that asks the user how many dice to roll
# program rolls all the dice once and prints out the sum

dice_rolls = []
dice_to_roll = int(input("How many dice would you like to roll? : "))
for x in range(dice_to_roll):
    y = random.randint(1,6)
    print(f"Dice rolled was {y}")
    dice_rolls.append(y)
print(f"Sum of the dice rolled was {sum(dice_rolls)}")



