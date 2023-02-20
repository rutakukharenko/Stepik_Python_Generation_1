# 15.2
# 15.2.1
from math import ceil
from math import log2

n = int(input())
iterations = ceil(log2(n))
print(iterations)

# Number guessing game.
import random

number = random.randint(1, 100)

print('Welcome to the number guessing game!')


def is_valid(num):
    result = False
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            result = True
        else:
            result = False
    return result


while True:
    answer = input('Enter the natural number 1 - 100: ')
    if not is_valid(answer):
        print('Please enter the natural number 1 - 100: ')
        continue
    else:
        answer = int(answer)
        if answer == number:
            print('Congratulations! You guessed!')
            break
        elif answer < number:
            print('The answer is less than number! Try again!')
        elif answer > number:
            print('The answer is more than number! Try again!')

print('Thank you for the game!')
