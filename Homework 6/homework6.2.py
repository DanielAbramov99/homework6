import random
from random import randint

lotto_number = (random.randint(1, 100))
print(lotto_number)
input_number: int = int(input("enter your number:"))
while True:
    if input_number < 1 or input_number > 100:
        input_number: int = int(input("illegal number,enter your number:"))
    elif input_number > lotto_number:
        input_number: int = int(input("your number is too big,enter number:"))
    elif input_number < lotto_number:
        input_number: int = int(input("your number is too small,enter number:"))
    else:
        print("bingo!")
        break
