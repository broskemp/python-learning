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

# write a program that asks the user to enter numbers until they input an empty string to quit
# at the end, the program prints out 5 greatest number in desc. order
# you can reverse the order of list items by doing sort w/ reverse=true argument

largestnumbers = []
while True:
    num = input("Enter a number : ")
    if num == "":
        break
    try:
        num = int(num)
        largestnumbers.append(num)
    except:
        print("Invalid input")
        continue

print("The 5 largest numbers in descending order is : ")
print(sorted(largestnumbers[-5:], reverse=True))

# write a program that asks the user for an integer and tells if the number is a prime number
# prime numbers are numbers that are only divisible by one or itself

primenumber = int(input("Enter a number to see if it's a prime number: "))

flag = False

if primenumber ==1:
    print(primenumber, "is not a prime number")
elif primenumber >1:
    # checking for factors
    for i in range(2, primenumber):
        if (primenumber % i) == 0:
            # if factor is found, set flag to True
            flag = True
            break
    if flag:
        print(primenumber, "is not a prime number")
    else:
        print(primenumber, "is a prime number")

# look at for loops a bit more

# write a program that asks the user for names of 5 cities one by one and puts em in list
# program prints out names one by one, one city per line, in the same order as input
# use for loop to read names, ask for names and for/in to iterate through the list

cities = []
city_entered = 0

while city_entered < 5:
    cityname = input("Enter a name of a city: ")
    cities.append(cityname)
    city_entered = city_entered + 1
else:
    print("Printing names...")

for i in range(0, len(cities)):
    print(cities[i])