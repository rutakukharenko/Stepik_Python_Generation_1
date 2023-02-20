# 7.2
# 7.2.1
m, n = int(input()), int(input())

for i in range(n, m + 1):
    print(i)

# 7.2.2
m, n = int(input()), int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(n, m - 1, -1):
        print(i)

# 7.2.3
m, n = int(input()), int(input())

for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)

# 7.2.4
m, n = int(input()), int(input())

for i in range(m, n + 1):
    if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
        print(i)

# 7.2.5
m, n = 10, int(input())

for i in range(1, m + 1):
    print(f'{n} x {i} = {n * i}')
