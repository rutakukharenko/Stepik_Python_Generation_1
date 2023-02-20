# 6.3
import math

# 6.3.1
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
euclidean_distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(euclidean_distance)

# 6.3.2
R = float(input())
S = math.pi * R ** 2
C = 2 * math.pi * R
print(S)
print(C)

# 6.3.3
a = float(input())
b = float(input())

arithmetical_mean = (a + b) / 2
geometric_mean = math.sqrt(a * b)
harmonic_mean = (2 * a * b) / (a + b)
root_mean_square = math.sqrt((a ** 2 + b ** 2) / 2)

print(arithmetical_mean)
print(geometric_mean)
print(harmonic_mean)
print(root_mean_square)

# 6.3.4
x = float(input())
x = (x * math.pi) / 180
result = math.sin(x) + math.cos(x) + (math.tan(x)) ** 2
print(result)

# 6.3.5
x = float(input())
result = math.ceil(x) + math.floor(x)
print(result)

# 6.3.6
a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - (4 * a * c)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    x = -b / (2 * a)
    if x == 0:
        print('0.0')
    else:
        print(x)
else:
    print('Нет корней')

# 6.3.7
n, a = int(input()), float(input())
S = (n * a ** 2) / (4 * math.tan(math.pi / n))
print(S)
