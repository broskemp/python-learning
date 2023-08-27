user = input('Enter your name: ')
print("Nice to meet you, " + user + "!")

fahrenheit_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print(f"The temperature in Celsius: {celsius:6.2f}")

