# 7.8
# 7.8.1
# 1
n = int(input())

for i in range(n):
    for _ in range(3):
        print(n, end=' ')
    print()

# 2
n = int(input())

for i in range(n):
    print((str(n) + ' ') * 3)

# 7.8.2
n = int(input())

for i in range(1, n + 1):
    for _ in range(5):
        print(i, end=' ')
    print()

# 7.8.3
n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        print(f'{i} + {j} = {i + j}')
    print()

# 7.8.4
n = int(input())

for i in range(n):
    k = (n // 2 + 1) - abs(n // 2 - i)
    for _ in range(k):
        print('*', end='')
    print()

# 7.8.5
n = int(input())

for i in range(1, n + 1):
    for j in range(i, i + 1):
        print(str(i) * j, end='')
    print()

# 7.8.6
total = 0
for n in range(1, 10):
    for k in range(1, 10):
        for m in range(1, 10):
            if 28 * n + 30 * k + 31 * m == 365:
                total += 1
                print('n =', n, 'k =', k, 'm =', m)

print('Общее количество натуральных решений =', total)

# 7.8.7
total = 0
for n in range(1, 100):
    for k in range(1, 100):
        for m in range(1, 100):
            if (10 * n + 5 * k + 0.5 * m == 100) and (n + k + m == 100):
                total += 1
                print('n =', n, 'k =', k, 'm =', m)

print('Общее количество натуральных решений =', total)
