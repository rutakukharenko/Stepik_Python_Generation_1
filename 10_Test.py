# 10 Test
# 10.1
s = 'Python rocks!'
print(len(s))

# 10.2
s = 'Python rocks!'
print(s[3])

# 10.3
s = 'Python rocks!'
print(s[1:5])

# 10.4
s = '    Python rocks!     '
print(s.strip())

# 10.5
s = 'Python rocks!'
print(s.upper())

# 10.6
s = 'Python rocks!'
print(s.replace('o', '@'))

# 10.7
string = input()
new_string = ''

for i in range(len(string)):
    if i % 3 != 0:
        new_string = new_string + string[i]

print(new_string)

# 10.8
string = input()
print(string.replace('1', 'one'))

# 10.9
string = input()
print(string.replace('@', ''))

# 10.10
# 1
string = input()
index = 0
count = 0

for i in range(len(string)):
    if string[i] == 'f' and count < 2:
        index = i
        count += 1

if count == 2:
    print(index)
elif count == 1:
    print(-1)
elif count == 0:
    print(-2)

# 2
string = input()
if string.count('f') == 1:
    print('-1')
elif string.count('f') == 0:
    print(-2)
elif string.count('f') > 1:
    string = string.replace('f', '+', 1)
    print(string.find('f'))

# 10.11
string = input()

index1 = string.find('h')
index2 = string.rfind('h')
print(string[:index1 + 1] + string[index2 - 1:index1:-1] + string[index2:])
