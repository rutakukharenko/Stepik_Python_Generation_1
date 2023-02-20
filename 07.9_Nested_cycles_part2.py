# 7.9
# 7.9.1
n = int(input())
total = 1

for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(total, end=' ')
        total = total + 1
    print()

# 7.9.2
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    for k in range(i - 1, 0, -1):
        print(k, sep='', end='')
    print()

# 7.9.3
a = int(input())
b = int(input())
counter = 0
largest = 0

for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total = total + j
        if (total >= counter) and (i >= largest):
            counter = total
            largest = i

print(largest, counter)

# 7.9.4
n = int(input())

for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    print(i, '+' * count, sep='')

# 7.9.5
n = int(input())

while n > 9:
    n = n // 10 + n % 10
print(n)

# 7.9.6
# 1
n = int(input())
sum_factorial = 0

for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum_factorial += factorial

print(sum_factorial)

# 2
n = int(input())
sum = 0
mult = 1

for i in range(1, n + 1):
    mult = mult * i
    sum = sum + mult

print(sum)

# 7.9.7
a = int(input())
b = int(input())

for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    if count == 2:
        print(i)
