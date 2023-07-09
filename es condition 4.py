# Compare those 2 numbers' absolute values and write X's absolute value
# greater than Y's absolute value Use abs function to do that
# eg.
# abs(-5) -> 5
# abs function makes all numbers positive

import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

if abs(number1) > abs(number2):
    print(f"absolute value of {number1} is greater than absolute value of {number2}")
elif abs(number1)<abs(number2):
    print(f"absolute value of {number2} is greater than absolute value of {number1}")
else:
    print(f"absolute value of {number2} is equals to absolute value of {number1}")

