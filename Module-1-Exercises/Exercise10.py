# elevator has 3 methods
# go to floor
# floor up
# floor down
# the elevator has to say what floor it is on after each "move"
# then test the elevator by going up to a floor and then back to the bottom

class Elevator:
    def __init__(self, bot_floor, top_floor):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.current_floor = 0

    def go_to_floor(self, target_floor):
        if target_floor < self.bot_floor or target_floor > self.top_floor:
            print("Invalid floor request.")
            return

        if target_floor == self.current_floor:
            print(f"Elevator is already on floor {target_floor}.")
            return

        while self.current_floor != target_floor:
            if target_floor > self.current_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")
        else:
            print("Elevator is already on the top floor")

    def floor_down(self):
        if self.current_floor > self.bot_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")
        else:
            print("Elevator is already on the bottom floor")


class Building:
    def __init__(self, top_floor, bot_floor, elevator_number):
        self.top_floor = top_floor
        self.bot_floor = bot_floor
        self.elevators = [Elevator(bot_floor, top_floor) for _ in range(elevator_number)]

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number")
            return

        elevator = self.elevators[elevator_number]
        print(f"Running Elevator {elevator_number} to floor {target_floor}")
        elevator.go_to_floor(target_floor)

    def fire_alarm(self):
        print("Fire alarm!! Returning all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Fire alarm triggered for Elevator {i}. Moving to the bottom floor.")
            elevator.go_to_floor(self.bot_floor)


BobW = Building(10, 1, 4)

BobW.run_elevator(0, 5)
BobW.run_elevator(1, 9)
BobW.run_elevator(2, 10)
BobW.run_elevator(0, 1)

BobW.fire_alarm()

# The last task for the exercise is in the Exercise9.py file, also linked in the submission
