import random

# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000

divisible = 0
while divisible < 1001:
    if divisible % 3 == 0:
        print(f"{divisible} is divisible by 3.")
    divisible = divisible + 1

# Write a program that converts inches to centimeters until the user inputs a negative value.

converter = int(input("Enter a pos value of inches to convert into centimeters. Neg to end the conversion. : "))
centimeterer = converter * 2.54
while converter >= 0:
    print(f"{converter} inches is {centimeterer} centimeters.")
    converter = int(input("Enter a pos value of inches to convert into centimeters. Neg to end the conversion. : "))
    centimeterer = converter * 2.54
print("Conversion stopped. Goodbye.")


# Write a program that asks the user to enter numbers until they enter an empty string.
# The program then prints out the smallest and largest number from the numbers it received.

largest = None
smallest = None

while True:
    num = input("Enter a number : ")
    if num == "":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print(f"The biggest number is {largest}")
print(f"The smallest number is {smallest}")

# Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number
# After each guess the program prints out a text: Too high, Too low or correct.
# The number must not be changed between guesses

randnumb = random.randrange(1, 10)
guess = int(input("Enter any number between 1-10: "))
while randnumb != guess:
    if guess < randnumb:
        print("Too low")
        guess = int(input("Enter a number between 1-10 again: "))
    elif guess > randnumb:
        print("Too high")
        guess = int(input("Enter a number between 1-10 again: "))
    else:
        break
print(f"You guessed correct! The correct number was {randnumb}")

# Write a program that asks the user for a username and password
# If either the password or the username are incorrect, the user is asked again
# This continues until the information is correct or the user enters the wrong information 5 times
# If the information is correct - Program prints "Welcome"
# If the information is incorrect 5 times in a row - Program prints "Access Denied"
# Username = python password = rules


attempt = 0
while attempt < 5:
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    if username != "python" or password != "rules":
        print("Invalid details")
        attempt = attempt + 1
    elif attempt == 5:
        break
    else:
        break

if attempt < 5:
    print("Welcome")
else:
    print("Access Denied")


# the 6th task I genuinely can't figure out - looking it up online the code needs
# the iteration function "for" and "in", which I don't know how they work just yet
# therefore, i'll try this again in exercise5.py