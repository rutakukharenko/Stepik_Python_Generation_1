# 4.3
# 4.3.1
n, k = int(input()), int(input())

if n > k:
    print('NO')
elif n < k:
    print('YES')
else:
    print("Don't know")

# 4.3.2
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
elif (a == b) or (b == c) or (a == c):
    print('Равнобедренный')
else:
    print('Разносторонний')

# 4.3.3
a, b, c = int(input()), int(input()), int(input())

if (b < a < c) or (c < a < b):
    print(a)
elif (a < b < c) or (c < b < a):
    print(b)
elif (a < c < b) or (b < c < a):
    print(c)

# 4.3.4
# 1
month = int(input())

if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
    print('31')
elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
    print('30')
elif month == 2:
    print('28')

# 2
x = int(input())

if x == 2:
    print(28)
elif (x < 8 and x % 2 == 0) or (x > 7 and x % 2 != 0):
    print(30)
else:
    print(31)

# 4.3.5
weight = int(input())

if weight < 60:
    print('Легкий вес')
elif 60 <= weight < 64:
    print('Первый полусредний вес')
elif 64 <= weight < 69:
    print('Полусредний вес')

# 4.3.6
# 1
a, b = int(input()), int(input())
action = input()

if b == 0 and action == '/':
    print('На ноль делить нельзя!')
else:
    if action == '+':
        print(a + b)
    elif action == '-':
        print(a - b)
    elif action == '*':
        print(a * b)
    elif action == '/':
        print(a / b)
    else:
        print('Неверная операция')

# 2
a, b = int(input()), int(input())
s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')

# 4.3.7
color1 = input()
color2 = input()

if ((color1 == 'красный') and (color2 == 'синий')) or ((color2 == 'красный') and (color1 == 'синий')):
    result = 'фиолетовый'
elif ((color1 == 'красный') and (color2 == 'желтый')) or ((color2 == 'красный') and (color1 == 'желтый')):
    result = 'оранжевый'
elif ((color1 == 'синий') and (color2 == 'желтый')) or ((color2 == 'синий') and (color1 == 'желтый')):
    result = 'зеленый'
elif (color1 == 'красный') and (color2 == 'красный'):
    result = 'красный'
elif (color1 == 'желтый') and (color2 == 'желтый'):
    result = 'желтый'
elif (color1 == 'синий') and (color2 == 'синий'):
    result = 'синий'
else:
    result = 'ошибка цвета'

print(result)

# 4.3.8
number = int(input())

if (number < 0) or (number > 36):
    result = 'ошибка ввода'
elif number == 0:
    result = 'зеленый'
elif (1 <= number <= 10) and (number % 2 != 0):
    result = 'красный'
elif (1 <= number <= 10) and (number % 2 == 0):
    result = 'черный'
elif (11 <= number <= 18) and (number % 2 != 0):
    result = 'черный'
elif (11 <= number <= 18) and (number % 2 == 0):
    result = 'красный'
elif (19 <= number <= 28) and (number % 2 != 0):
    result = 'красный'
elif (19 <= number <= 28) and (number % 2 == 0):
    result = 'черный'
elif (29 <= number <= 36) and (number % 2 != 0):
    result = 'черный'
elif (29 <= number <= 36) and (number % 2 == 0):
    result = 'красный'

print(result)

# 4.3.9
# 1
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a2 < a1:
    if b2 < a1:
        print('пустое множество')
    elif b2 == a1:
        print(b2)
    elif a1 < b2 <= b1:
        print(a1, b2)
    elif b2 > b1:
        print(a1, b1)
elif a2 == a1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 < b1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('пустое множество')

# 2
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if min(b1, b2) < max(a1, a2):
    print('пустое множество')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))
