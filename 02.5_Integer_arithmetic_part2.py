# 2.5
# "ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ"         "ОСТАТОК ОТ ДЕЛЕНИЯ"                          "КАК ЭТО РАБОТАЕТ"
# 19 // 5 = 3                     19 % 5 = 4                     ==>>           19 - (5 * 3) = 4
# 19 // -5 = -4                   19 % -5 = -1                   ==>>           19 - (-5 * -4) = 19 - (20) = -1
# -19 // 5 = -4                   -19 % 5 = 1                    ==>>           -19 - (5 * -4) = -19 - (-20) = -19 + 20 = 1
# -19 // -5 = 3                   -19 % -5 = -4                  ==>>           -19 - (-5 * 3) = -19 - (-15) = -19 + 15 = -4

# 2.5.1
b_1 = int(input())
q = int(input())
n = int(input())

b = b_1 * (q ** (n - 1))

print(b)

# 2.5.2
centimeters = int(input())
meters = centimeters // 100
print(meters)

# 2.5.3
num_1 = int(input())
num_2 = int(input())

print(num_2 // num_1)
print(num_2 % num_1)

# 2.5.4
# 1
n = int(input())
result = (-n // 2) * (-1)
print(result)

# 2
n = int(input())
print((n + 1) // 2)

# 2.5.5
# 1
n = int(input())
result = (-n // 4) * (-1)
print(result)

# 2
a = int(input())
print((a - 1) // 4 + 1)

# 2.5.6
minutes = int(input())
print(f'{minutes} мин - это {minutes // 60} час {minutes % 60} минут.')

# 2.5.7
num = int(input())

c = num % 10  # Last digit.
b = (num % 100) // 10  # Middle digit.
a = num // 100  # First digit.

print(f'Сумма цифр = {a + b + c}')
print(f'Произведение цифр = {a * b * c}')

# 2.5.8
num = int(input())

c = num % 10  # Last digit.
b = (num % 100) // 10  # Middle digit.
a = num // 100  # First digit.

print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')

# 2.5.9
num = int(input())

d = num % 10  # Last digit.
c = (num % 100) // 10  # Middle digit.
b = (num % 1000) // 100  # Middle digit.
a = (num % 10000) // 1000  # First digit.

print(f'Цифра в позиции тысяч равна {a}')
print(f'Цифра в позиции сотен равна {b}')
print(f'Цифра в позиции десятков равна {c}')
print(f'Цифра в позиции единиц равна {d}')
