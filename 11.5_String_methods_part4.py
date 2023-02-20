# 11.5
# 11.5.1
string = input()
list = string.split()

for word in list:
    print(word)

# 11.5.2
string = input()
full_name = string.split()

for word in full_name:
    print(word[0], end='.')

# 11.5.3
path = input().split('\\')

for dir in path:
    print(dir)

# 11.5.4
numbers = input().split()

for num in numbers:
    print('+' * int(num))

# 11.5.5
ip_address = input().split('.')
flag = True

for num in ip_address:
    if not (0 <= int(num) <= 255):
        flag = False
        break

if flag:
    print('ДА')
else:
    print('НЕТ')

# 11.5.6
text = list(input())
separator = input()
print(f'{separator}'.join(text))

# 11.5.7
string = input()
numbers = string.split()
count_pairs = 0

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count_pairs += 1

print(count_pairs)
