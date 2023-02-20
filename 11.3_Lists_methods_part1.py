# 11.3
# 11.3.1
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
           12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])

if (5 in numbers) and (17 in numbers):
    print('YES')
else:
    print('NO')

del numbers[0]
del numbers[-1]
print(numbers)

# 11.3.2
n = int(input())
list = []

for i in range(n):
    list.append(input())

print(list)

# 11.3.3
# 1
n = 26
symbol = ord('a')
list = []

for i in range(1, n + 1):
    list.append(chr(symbol) * i)
    symbol += 1

print(list)

# 2
l = []
for i in range(ord('z') - ord('a') + 1):
    l.append(chr(ord('a') + i) * (i + 1))
print(l)

# 11.3.4
n = int(input())
list = []

for i in range(n):
    num = int(input()) ** 3
    list.append(num)

print(list)

# 11.3.5
n = int(input())
list = []

for i in range(1, n + 1):
    if n % i == 0:
        list.append(i)

print(list)

# 11.3.6
n = int(input())
numbers = []
sum = []

for _ in range(n):
    numbers.append(int(input()))

for i in range(len(numbers) - 1):
    sum.append(numbers[i] + numbers[i + 1])

print(sum)

# 11.3.7
n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))
del numbers[1::2]

print(numbers)

# 11.3.8
n = int(input())
strings = []

for _ in range(n):
    strings.append(input())

k = int(input())

for string in strings:
    if len(string) >= k:
        print(string[k - 1], end='')

# 11.3.9
n = int(input())
chars = []

for _ in range(n):
    chars.extend(input())

print(chars)
