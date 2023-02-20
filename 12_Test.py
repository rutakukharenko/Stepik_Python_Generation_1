# 12 Test
# 12.1
list_input = [i for i in range(2, int(input()) + 1, 2)]
print(list_input)

# 12.2
# 1
L = input().split()
M = input().split()
result = []

for i in range(len(L)):
    result.append(int(L[i]) + int(M[i]))

print(*result)

# 2
L = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]

result = [L[i] + M[i] for i in range(len(L))]

print(*result)

# 12.3
numbers = [int(i) for i in input().split()]
print(*numbers, sep='+', end='=')
print(sum(numbers))

# 12.4
# 1
phone_number = input()
phone_num_list = phone_number.split('-')
flag = False

if len(phone_num_list) == 3:
    if (len(phone_num_list[0]) == 3 and phone_num_list[0].isdigit()) and (
            len(phone_num_list[1]) == 3 and phone_num_list[1].isdigit()) and (
            len(phone_num_list[2]) == 4 and phone_num_list[2].isdigit()):
        flag = True
    else:
        flag = False
elif len(phone_num_list) == 4:
    if (int(phone_num_list[0]) == 7 and len(phone_num_list[0]) == 1 and phone_num_list[0].isdigit()) and (
            len(phone_num_list[1]) == 3 and phone_num_list[1].isdigit()) and (
            len(phone_num_list[2]) == 3 and phone_num_list[2].isdigit()) and (
            len(phone_num_list[3]) == 4 and phone_num_list[3].isdigit()):
        flag = True
    else:
        flag = False

if flag:
    print('YES')
else:
    print('NO')

# 2
import re

s = input()
pattern = r"7?-?\d{3}-\d{3}-\d{4}"
print('YES' if s in re.findall(pattern, s) else 'NO')

# 3
n = input().split("-")
c = [len(i) for i in n]
if c == [3, 3, 4] and ''.join(n).isdigit():
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
    print("YES")
else:
    print("NO")

# 12.5
text_list = [len(word) for word in input().split()]
print(max(text_list))

# 12.5
text_list = [word[1:] + word[0] + 'ки' for word in input().split()]
print(*text_list)
