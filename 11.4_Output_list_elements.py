# 11.4
# 11.4.1
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
sum = 0

for n in numbers:
    sum = sum + n ** 2

print(sum)

# 11.4.2
n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))
    print(numbers[i])

print()

for n in numbers:
    print(n ** 2 + 2 * n + 1)

# 11.4.3
n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

del numbers[numbers.index(max(numbers))]
del numbers[numbers.index(min(numbers))]

print(*numbers, sep='\n')

# 11.4.4
n = int(input())
strings = []

for _ in range(n):
    string = input()
    if string not in strings:
        strings.append(string)

print(*strings, sep='\n')

# 11.4.5
n = int(input())
data = []

for _ in range(n):
    data.append(input())

search = input()

for item in data:
    if search.lower() in item.lower():
        print(item)

# 11.4.6
n = int(input())
responses = []
for _ in range(n):
    responses.append(input())

k = int(input())
requests = []
for _ in range(k):
    requests.append(input())

for res in responses:
    for req in requests:
        if req.lower() not in res.lower():
            break
    else:
        print(res)

# 11.4.7
n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))

for element in list:
    if element < 0:
        print(element)

for element in list:
    if element == 0:
        print(element)

for element in list:
    if element > 0:
        print(element)
