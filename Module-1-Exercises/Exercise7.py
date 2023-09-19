# write a program to calculate what season it is within the 12 months

seasons = ("spring", "summer", "autumn", "winter")
(first, second, third, fourth) = seasons
month_number = int(input("Enter the number of a month (1-12): "))
if month_number == 3 or month_number == 4 or month_number == 5:
    print(f"This month's season is {first}")
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(f"This month's season is {second}")
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(f"This month's season is {third}")
elif month_number == 1 or month_number == 2 or month_number == 12:
    print(f"This month's season is {fourth}")
else:
    print("Invalid number of month. Please enter a valid number. (1-12).")


# write a program that keeps asking for names until an empty string is written
# the program then prints out new name or existing name while reading out each name written
# the program finally lists out the input names one by one

names = set()

while True:
    nameinput = input("Enter a name : ")
    if nameinput == "":
        break
    else:
        if nameinput in names:
            print(f"{nameinput} is an existing name")
        else:
            print(f"{nameinput} is a new name")
            names.add(nameinput)

for n in names:
    print(n)


# write a program for fetching and storing airport data
# the program asks the user if they want to:
# enter a new airport, fetch an existing airport or quit
# new airport asks the user to enter ICAO code and name of airport
# fetch airport asks user for ICAO code and prints out name
# quit will end the program

airports = {"EFHK": "Helsinki-Vantaa Airport",
            "KDAA": "Davison Army Air Field",
            "YNRC": "Naracoorte Airport"}

while True:
    airport_input = int(input("What would you like to do? 1) New airport 2) Fetch an airport 3) Quit : "))
    if airport_input == 3:
        break
    elif airport_input == 1:
        new_airport_name = input("What is the name of the new airport? : ")
        new_airport_code = input("What is the code of the new airport? : ").upper()
        airports[new_airport_code] = new_airport_name
    elif airport_input == 2:
        current_airport_code = input("What is the code of the airport you're looking for? : ").upper()
        if current_airport_code in airports:
            print(f"{current_airport_code} is {airports[current_airport_code]}")
    else:
        print("Please enter a valid number. 1 / 2 / 3")
