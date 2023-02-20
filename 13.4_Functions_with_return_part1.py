# 13.4
# 13.4.1
def convert_to_miles(km):
    miles = km * 0.6214  # мили = километры * 0.6214.
    return miles


num = int(input())

print(convert_to_miles(num))

# 13.4.2
def get_days(month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = months[month - 1]
    return result


num = int(input())

print(get_days(num))

# 13.4.3
# 1
def get_factors(num):
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers


n = int(input())

print(get_factors(n))

# 2
def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]


n = int(input())

print(get_factors(n))

# 13.4.4
# 1
def number_of_factors(num):
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return len(dividers)


n = int(input())

print(number_of_factors(n))

# 2
def get_factors(num):
    return len([n for n in range(1, num + 1) if num % n == 0])


n = int(input())

print(get_factors(n))

# 13.4.5
def find_all(target, symbol):
    result = []
    for i in range(len(target)):
        if target[i] == symbol:
            result.append(i)
    return result


s = input()
char = input()

print(find_all(s, char))

# 13.4.6
def merge(list1, list2):
    result = list1 + list2
    result.sort()
    return result


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))

# 13.4.7
n = int(input())
list = []

for i in range(n):
    numbers = [int(c) for c in input().split()]
    list = list + numbers

list.sort()

print(*list)