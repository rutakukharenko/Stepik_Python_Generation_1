# 9.3
# 9.3.1
name = input()
name_correct = name.title()

if name == name_correct:
    print('YES')
else:
    print('NO')

# 9.3.2
print(input().swapcase())

# 9.3.3
text = input().lower()
check = 'хорош'

if check in text:
    print('YES')
else:
    print('NO')

# 9.3.4
# 1
s, counter = input(), 0
for i in s:
    if i != i.upper():
        counter += 1
print(counter)

# 2
text = input()
check_string = 'abcdefghijklmnopqrstuvwxyz'
count = 0

for c in text:
    if c in check_string:
        count += 1

print(count)
