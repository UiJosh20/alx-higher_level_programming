#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
last_digit = number % 10 if num >= 0 else ((-num % 10) * -1)
msg = f"Last digit of {num} is {last_digit}"

if last_digit == 0:
    print(f"{msg} and is 0")
elif last_digit > 5 and last_digit % 10 != 0:
    print(f"{msg} and is greater than 5")
else:
   print(f"{msg} and is less than 6 and not 0")
