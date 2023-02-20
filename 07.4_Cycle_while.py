# 7.4
# 7.4.1
# while True.
sentence = input()

while sentence != 'КОНЕЦ':
    print(sentence)
    sentence = input()

# 7.4.2
# while True.
sentence = input()

while (sentence != 'КОНЕЦ') and (sentence != 'конец'):
    print(sentence)
    sentence = input()

# 7.4.3
# while True.
sentence = input()
counter = 0

while (sentence != 'стоп') and (sentence != 'хватит') and (sentence != 'достаточно'):
    counter = counter + 1
    sentence = input()

print(counter)

# 7.4.4
# while True.
num = int(input())

while num % 7 == 0:
    print(num)
    num = int(input())

# 7.4.5
# while True.
num = int(input())
sum = 0

while num >= 0:
    sum = sum + num
    num = int(input())

print(sum)

# 7.4.6
# while True.
num = int(input())
counter = 0

while (num > 0) and (num <= 5):
    if num == 5:
        counter = counter + 1
    num = int(input())

print(counter)

# 7.4.7
# while True.
n = int(input())
i = 0

while n >= 25:
    n = n - 25
    i = i + 1
while n >= 10:
    n = n - 10
    i = i + 1
while n >= 5:
    n = n - 5
    i = i + 1
while n >= 1:
    n = n - 1
    i = i + 1

print(i)
