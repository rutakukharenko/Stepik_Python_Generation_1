# 11.6
# 11.6.1
numbers = [8, 9, 10, 11]
numbers2 = [4, 5, 6]
numbers[1] = 17
numbers.extend(numbers2)
del numbers[0]
numbers = numbers * 2
numbers.insert(3, 25)
print(numbers)

# 11.6.2
string_list = input().split()
numbers = []

for char in string_list:
    numbers.append(int(char))

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(*numbers)

# 11.6.3
text = input().lower()

text = text.split()
articles_count = text.count('a') + text.count('an') + text.count('the')

print(f'Общее количество артиклей: {articles_count}')

# 11.6.4
n = int(input()[1:])

for i in range(n):
    code_string = input().split('#')
    code_string = code_string[0].rstrip()
    print(code_string)

# 11.6.5
numbers_string = input().split()
numbers = []

for num in numbers_string:
    numbers.append(int(num))

numbers.sort()
print(*numbers, sep=' ')

numbers.sort(reverse=True)
print(*numbers, sep=' ')
