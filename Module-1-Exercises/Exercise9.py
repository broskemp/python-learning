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
