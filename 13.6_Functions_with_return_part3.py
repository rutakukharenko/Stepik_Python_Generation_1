# 13.6
import math

# 13.6.1
def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
middle_point_x, middle_point_y = get_middle_point(x1, y1, x2, y2)

print(middle_point_x, middle_point_y)

# 13.6.2
def get_circle(radius):
    C = 2 * math.pi * radius
    S = math.pi * radius ** 2
    return C, S


radius = float(input())
C, S = get_circle(radius)

print(C, S)

# 13.6.3
def solve(a, b, c):
    d = b ** 2 - (4 * a * c)

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return min(x1, x2), max(x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        return x, x
    else:
        return 'Нет корней'


a, b, c = float(input()), float(input()), float(input())
x1, x2 = solve(a, b, c)

print(x1, x2)
