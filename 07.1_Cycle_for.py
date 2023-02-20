# 7.1
# 7.1.1
for i in range(10):
    print('Python is awesome!')

# 7.1.2
string1, iterations = input(), int(input())

for i in range(iterations):
    print(string1)

# 7.1.3
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

# 7.1.4
n = int(input())

for i in range(n):
    print('*******************')

# 7.1.5
string1 = input()

for i in range(10):
    print(f'{i} {string1}')

# 7.1.6
# 1
n = int(input())

print('Квадрат числа 0 равен 0')

for i in range(n):
    print('Квадрат числа', i + 1, 'равен', (i + 1) ** 2)

# 2
n = int(input())

for i in range(0, n + 1):
    print(f'Квадрат числа {i} равен {i ** 2}')

# 7.1.7
# 1
n = int(input())
a = '*'

for i in range(n):
    result = a * n
    print(result)
    n = n - 1

# 2
n = int(input())

for i in range(n, 1, -1):
    print('*' * i)

# 7.1.8
m, p, n = int(input()), int(input()), int(input())
p = p / 100

for i in range(n):
    print(f'{i + 1} {m}')
    m = m + (m * p)
