# 7.5
'''
Обработка цифр числа. Пример кода.

n = int(input())
while n != 0:  # Пока в числе есть цифры.
    last_digit = n % 10  # Получить последнюю цифру.
    # Код обработки последней цифры.
    n = n // 10  # Удалить последнюю цифру из числа.
'''

# 7.5.1
num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10

# 7.5.2
num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit, end='')
    num = num // 10

# 7.5.3
# 1
num = int(input())
last_digit = num % 10
max = last_digit
min = last_digit

while num != 0:
    last_digit = num % 10
    if last_digit > max:
        max = last_digit
    if last_digit < min:
        min = last_digit
    num = num // 10

print(f'Максимальная цифра равна {max}')
print(f'Минимальная цифра равна {min}')

# 2
num = int(input())
number = []

while num != 0:
    last_digit = num % 10
    number.append(last_digit)
    num = num // 10

number.sort()
max = number[-1]
min = number[0]

print(f'Максимальная цифра равна {max}')
print(f'Минимальная цифра равна {min}')

# 7.5.4
num = int(input())
first_digit = 0
last_digit = num % 10
sum = 0
counter = 0
prod = 1

while num != 0:
    digit = num % 10

    sum = sum + digit
    counter = counter + 1
    prod = prod * digit

    if 0 < num < 10:
        first_digit = num

    num = num // 10

arithmetical_mean = sum / counter
sum_first_last = first_digit + last_digit

print(sum)
print(counter)
print(prod)
print(arithmetical_mean)
print(first_digit)
print(sum_first_last)

# 7.5.5
# 1
num = int(input())

while num > 9:
    last_digit = num % 10
    num = num // 10

print(last_digit)

# 2
num = int(input())
number = []

while num != 0:
    last_digit = num % 10
    number.append(last_digit)
    num = num // 10

number.reverse()
second_digit = number[1]

print(second_digit)

# 7.5.6
num = int(input())
last_digit = num % 10
flag = True

while num != 0:
    digit = num % 10
    if digit != last_digit:
        flag = False
    num = num // 10

if flag:
    print('YES')
else:
    print('NO')

# 7.5.7
num = int(input())
flag = True

while num > 9:
    last_digit = num % 10
    prev_last_digit = (num // 10) % 10
    if prev_last_digit < last_digit:
        flag = False
    num = num // 10

if flag:
    print('YES')
else:
    print('NO')
