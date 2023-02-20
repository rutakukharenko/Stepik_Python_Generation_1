# 9.6
# 9.6.1
a, b = int(input()), int(input())

for i in range(a, b + 1):
    print(chr(i), end=' ')

# 9.6.2
string1 = input()

for c in string1:
    print(ord(c), end=' ')

# 9.6.3
n = int(input())
string = input()

for char in string:
    if (ord(char) - n) < ord('a'):
        print(chr(ord(char) - n + 26), end='')
    else:
        print(chr(ord(char) - n), end='')
