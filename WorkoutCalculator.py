
workouts = []
while True:
    ans = int(input("What would you like to do, "
                    "\n 1) Calculate the per week weight for a workout; 2) Check your calculations 3) Quit : "))
    if ans == 3:
        print("Goodbye")
        break
    elif ans == 1:
        while True:
            workout = input('Enter name of workout: ')
            if workout == "":
                print("Please enter a workout name")
            else:
                max_weight = float(input(f"Enter the maximum weight of {workout}: "))
                deload_weight = float(input(f"Enter the deload weight of {workout}: "))
                weight_delta = max_weight - deload_weight
                per_week = weight_delta / 5
                starting_weight = deload_weight + per_week
                print(f"The per week increase for {workout} is {per_week} with a starting weight of {starting_weight}")
                workouts.append(f"The per week increase for {workout} is {per_week} with a starting weight of {starting_weight}")
                break
    elif ans == 2:
        for x in range(len(workouts)):
            print(workouts[x])
    else:
        print("Please enter a valid number.")