import random
code3 = random.randint(1, 10**3)
code3gen = '{:03}'.format(code3)
code4 = random.randint(1, 10**4)
code4gen = '{:04}'.format(code4)

answer = int(input("How long of a code would you like to generate? 3 or 4? = "))
if answer == 3:
    print(f"Your 3 digit code is {code3gen}")
elif answer == 4:
    print(f"Your 4 digit code is {code4gen}")
else:
    print("Please enter 3 or 4.")