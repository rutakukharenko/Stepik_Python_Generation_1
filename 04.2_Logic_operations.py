# 4.2
# 4.2.1
x = int(input())

if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4.2.2
x = int(input())

if (x <= -3) or (x >= 7):
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4.2.3
x = int(input())

if (-30 < x <= -2) or (7 < x <= 25):
    print('Принадлежит')
else:
    print('Не принадлежит')

# 4.2.4
number = int(input())

if (1000 <= number <= 9999) and ((number % 7 == 0) or (number % 17 == 0)):
    print('YES')
else:
    print('NO')

# 4.2.5
a, b, c = int(input()), int(input()), int(input())

if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')

# 4.2.6
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')

# 4.2.7
# Ход ладьи.
x, y, x1, y1 = int(input()), int(input()), int(input()), int(input())

if (x == x1) or (y == y1):
    print('YES')
else:
    print('NO')

# 4.2.8
# Ход короля.
# 1
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print('YES')
else:
    print('NO')

# 2
x = int(input())
y = int(input())
x_user = int(input())
y_user = int(input())

x1 = x + 1
x2 = x - 1
y1 = y + 1
y2 = y - 1

if (x_user == x and y_user == y1) or (x_user == x1 and y_user == y1) or (x_user == x1 and y_user == y) or (
        x_user == x1 and y_user == y2) or (x_user == x and y_user == y2) or (x_user == x2 and y_user == y2) or (
        x_user == x2 and y_user == y) or (x_user == x2 and y_user == y1):
    print('YES')
else:
    print('NO')
