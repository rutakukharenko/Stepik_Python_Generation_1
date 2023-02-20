# 7.3
import math

# 7.3.1
a, b = int(input()), int(input())
counter = 0

for i in range(a, b + 1):
    if (i ** 3 % 10 == 4) or (i ** 3 % 10 == 9):
        counter = counter + 1

print(counter)

# 7.3.2
n = int(input())
total = 0

for _ in range(n):
    a = int(input())
    total = total + a

print(total)

# 7.3.3
n = int(input())
total = 0

for i in range(1, n + 1):
    total = total + 1 / i

result = total - math.log(n, math.e)

print(result)

# 7.3.4
n = int(input())
total = 0

for i in range(1, n + 1):
    if (i ** 2 % 10 == 2) or (i ** 2 % 10 == 5) or (i ** 2 % 10 == 8):
        total = total + i

print(total)

# 7.3.5
n = int(input())
result = 1

for i in range(1, n + 1):
    result = result * i

print(result)

# 7.3.6
n = 10
result = 1

for i in range(1, n + 1):
    a = int(input())
    if a != 0:
        result = result * a

print(result)

# 7.3.7
n = int(input())
result = 0

for i in range(1, n + 1):
    if n % i == 0:
        result = result + i

print(result)

# 7.3.8
n = int(input())
result = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        result = result - i
    else:
        result = result + i

print(result)

# 7.3.9
# 1
n = int(input())
largest = 0
pre_largest = 0

for i in range(1, n + 1):
    number = int(input())
    if number > largest:
        pre_largest = largest
        largest = number
    elif number < largest:
        if number > pre_largest:
            pre_largest = number

print(largest)
print(pre_largest)

# 2
n = int(input())
array = []

for i in range(1, n + 1):
    number = int(input())
    array.append(number)

array.sort()
largest = array[-1]
pre_largest = array[-2]

print(largest)
print(pre_largest)

# 7.3.10
n = 10
flag = True

for _ in range(1, n + 1):
    num = int(input())
    if num % 2 != 0:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')

# 7.3.11
# Последовательность Фибоначчи.
n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
