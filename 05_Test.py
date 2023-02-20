# 5 Test
# 5.1
year = int(input())

if year % 100 == 0:
    print('YES')
else:
    print('NO')

# 5.2
x, y, x1, y1 = int(input()), int(input()), int(input()), int(input())

if (x + y + x1 + y1) % 2 == 0:
    print('YES')
else:
    print('NO')

# 5.3
age, sex = int(input()), input()

if (10 <= age <= 15) and (sex == 'f'):
    print('YES')
else:
    print('NO')

# 5.4
# 1
x = int(input())

if not (1 <= x <= 10):
    print('ошибка')
elif x == 1:
    print('I')
elif x == 2:
    print('II')
elif x == 3:
    print('III')
elif x == 4:
    print('IV')
elif x == 5:
    print('V')
elif x == 6:
    print('VI')
elif x == 7:
    print('VII')
elif x == 8:
    print('VIII')
elif x == 9:
    print('IX')
elif x == 10:
    print('X')

# 2
a = int(input())
num = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
if a < 0 or a > 10:
    print("ошибка")
else:
    print(num[a])

# 5.5
x = int(input())

if x % 2 != 0:
    print('YES')
elif x % 2 == 0 and 2 <= x <= 5:
    print('NO')
elif x % 2 == 0 and 6 <= x <= 20:
    print('YES')
elif x % 2 == 0 and x > 20:
    print('NO')

# 5.6
# Ход слона.
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')

# 5.7
# Ход коня.
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')

# 5.8
# Ход ферзя.
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

diagonal_1 = (x1 + y1 == x2 + y2)
diagonal_2 = (x1 + y2 == y1 + x2)
vertical = (y1 == y2)
horizontal = (x1 == x2)

if diagonal_1 or diagonal_2 or vertical or horizontal:
    print("YES")
else:
    print("NO")
