# Ask for length of a zander in centimeters
# If zander < 42cm - must be released and user is notified how much below the limit the fish was

zander = int(input("How big is the zander? Insert the size in centimeters: "))
if zander < 42:
    print("The zander is too small.")
    print(f"The zander is {42 - zander} centimeters smaller than the allowed limit.")
    print("Please release the poor fish.")
elif zander == 42:
    print("The zander is exactly 42 centimeters big - right at the legal limit. You may keep it.")
else:
    print(f"The zander is bigger than the legal limit at {zander} centimeters, nice job!")

# Ask the user for a cabin class of a cruise ship
# Then prints out a written description
# If the class doesn't exist, it displays an error

print("Welcome to the SS Burya. Here are the cabin classes available.")
print("LUX, A, B, C")
cabin = input("Which cabin would you like to know more about?: ")
if cabin == "LUX" or "lux":
    print("LUX is a luxurious upper-deck cabin with a balcony.")
elif cabin == "A" or "a":
    print("A is a regular cabin above the car deck with a window")
elif cabin == "B" or "b":
    print("B is a regular cabin above the car deck without a window")
elif cabin == "C" or "c":
    print("C is a regular cabin below the car deck without a window")
else:
    print("Invalid cabin class.")

# Ask for biological sex and hemoglobin value (g/l)
# The program notifies if the value is high, low or normal.
# Normal value for males - 134-167 g/l
# Normal value for females - 117-155 g/l

sex = str(input("What is your biological sex for the hemoglobin test? M/F : "))
hemoglobin = int(input("What is your current hemoglobin value? Enter only numbers : "))

if sex == "m":
    print("You are a male.")
elif sex == "f":
    print("You are a female.")
else:
    print("Please enter a valid biological sex.")

if hemoglobin < 134 and sex == "m":
    print("Your hemoglobin is too low.")
elif hemoglobin > 167 and sex == "m":
    print("Your hemoglobin is too high.")
elif 134 <= hemoglobin <= 167 and sex == "m":
    print("Your hemoglobin is normal.")
elif hemoglobin < 117 and sex == "f":
    print("Your hemoglobin is too low.")
elif hemoglobin > 155 and sex == "f":
    print("Your hemoglobin is too high.")
elif hemoglobin >= 117 and (hemoglobin <= 155) and sex == "f":
    print("Your hemoglobin is normal.")
else:
    print("Please enter a number.")


# Write a program that asks the user for a year
# Notifies the user if the input year is a leap year (divisible by 4)
# However, if the year is divisible by 100, it also has to be divisible by 400 to be a leap year

leapyear = int(input("Please enter a year to calculate if it is a leap year or not. : "))
if leapyear % 400 == 0:
    print(f"{leapyear} is a leap year.")
elif leapyear % 100 == 0:
    print(f"{leapyear} is not a leap year.")
elif leapyear % 4 == 0:
    print(f"{leapyear} is a leap year.")
else:
    print(f"{leapyear} is not a leap year.")
