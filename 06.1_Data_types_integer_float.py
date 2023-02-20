# 6.1
# 6.1.1
a, b = float(input()), float(input())
S = 0.5 * a * b
print(S)

# 6.1.2
S, V1, V2 = float(input()), float(input()), float(input())

V = V1 + V2
T = S / V

print(T)

# 6.1.3
num = float(input())

if num == 0:
    print('Обратного числа не существует')
else:
    print(num ** (-1))

# 6.1.4
F = float(input())
C = (5 / 9) * (F - 32)
print(C)

# 6.1.5
dog_age = int(input())

if dog_age == 1:
    age = dog_age * 10.5
else:
    age = (2 * 10.5) + ((dog_age - 2) * 4)

print(age)

# 6.1.6
n = float(input())
print((n - int(n)) * 10)

# 6.1.7
n = float(input())
print(n - int(n))

# 6.1.8
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
print(f'Наименьшее число = {min(a, b, c, d, e)}')
print(f'Наибольшее число = {max(a, b, c, d, e)}')

# 6.1.9
a, b, c = int(input()), int(input()), int(input())

max_n = max(a, b, c)
min_n = min(a, b, c)
mid_n = (a + b + c) - (max_n + min_n)

print(max_n)
print(mid_n)
print(min_n)

# 6.1.10
num = int(input())

c = num % 10  # Last digit.
b = (num % 100) // 10  # Middle digit.
a = num // 100  # First digit.

max_n = max(a, b, c)
min_n = min(a, b, c)
mid_n = (a + b + c) - (max_n + min_n)

if (max_n - min_n) == mid_n:
    print('Число интересное')
else:
    print('Число неинтересное')

# 6.1.11
a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
sum = abs(a) + abs(b) + abs(c) + abs(d) + abs(e)
print(sum)

# 6.1.12
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
manhattan = abs(p1 - q1) + abs(p2 - q2)
print(manhattan)
