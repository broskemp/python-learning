import random


class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        self.current_speed = max(0, min(new_speed, self.max_speed))

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * hours)


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery):
        self.battery = battery
        super().__init__(reg_number, max_speed)


class GasCar(Car):
    def __init__(self, reg_number, max_speed, gasoline):
        self.gasoline = gasoline
        super().__init__(reg_number, max_speed)


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.cars = car_list

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)

    def print_status(self):
        print(f"{'Car':<15} {'Speed (km/h)':<15} {'Distance (km)':<20}")
        for car in self.cars:
            print(f"{car.reg_number:<15} {car.current_speed:<15} {car.travelled_distance:<20}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


def create_car(reg_number, maximum_speed):
    return Car(reg_number, maximum_speed)


# Exercise 9
cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
race_over = False
hour = 0
while not race_over:
    hour += 1
    print(f"Hour of race : {hour}")

    for car in cars:
        change_speed = random.randint(-10, 15)
        car.accelerate(change_speed)

        car.drive(1)

        print(f"{car.reg_number}:"
              f"Speed: {car.current_speed} "
              f"Distance: {car.travelled_distance}")

        if car.travelled_distance >= 10000:
            race_over = True
            break

print("Race finished! Here are the results:")
print(f"{'Registration number':<15} {'Maximum speed (km/h)':<20} {'Distance traveled (km)':<25}")
for car in cars:
    print(f"{car.reg_number:<15} "
          f"Final speed: {car.current_speed:<20} "
          f"Final distance: {car.travelled_distance:<25}")

# Exercise 10 task 4
race_cars = [create_car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
grand_derby = Race("Grand Demolition Derby", 8000, race_cars)

hour = 0

while not grand_derby.race_finished():
    grand_derby.hour_passes()
    hour += 1
    if hour % 10 == 0:
        print(f"Race Progress After {hour} Hours:")
        grand_derby.print_status()

print("Final Race Results:")
grand_derby.print_status()

# Exercise 11 task 2
Tesla = ElectricCar("ABC-15",180,52.5)
Jeep = GasCar("ACD-123", 165,32.3)

Tesla.accelerate(170)
Jeep.accelerate(150)

Tesla.drive(5)
Jeep.drive(5)

print(f"The Tesla has driven for {Tesla.travelled_distance} kilometers")
print(f"The Jeep has driven for {Jeep.travelled_distance} kilometers")