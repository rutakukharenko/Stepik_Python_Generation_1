# 4.1
# 4.1.1
password_1, password_2 = input(), input()

if password_1 == password_2:
    print('Пароль принят')
else:
    print('Пароль не принят')

# 4.1.2
num = int(input())

if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# 4.1.3
num = int(input())

d = num % 10  # Last digit.
c = (num % 100) // 10  # Middle digit.
b = (num % 1000) // 100  # Middle digit.
a = (num % 10000) // 1000  # First digit.

if (a + d) == (b - c):
    print('ДА')
else:
    print('НЕТ')

# 4.1.4
age = int(input())

if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# 4.1.5
num_1, num_2, num_3 = int(input()), int(input()), int(input())

if (num_3 - num_2) == (num_2 - num_1):
    print('YES')
else:
    print('NO')

# 4.1.6
num_1, num_2 = int(input()), int(input())

if num_1 < num_2:
    print(num_1)
else:
    print(num_2)

# 4.1.7
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c

print(a)

# 4.1.8
age = int(input())

if age <= 13:
    print('детство')
elif 14 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
elif age >= 60:
    print('старость')

# 4.1.9
a, b, c = int(input()), int(input()), int(input())
sum = 0

if a > 0:
    sum = sum + a
if b > 0:
    sum = sum + b
if c > 0:
    sum = sum + c

print(sum)
