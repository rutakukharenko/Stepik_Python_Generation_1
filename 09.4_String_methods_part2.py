# 9.4
# 9.4.1
string1 = input()
words = string1.count(' ') + 1
print(words)

# 9.4.2
# 1
string = input()
string = string.lower()
print('Аденин:', string.count('а'))
print('Гуанин:', string.count('г'))
print('Цитозин:', string.count('ц'))
print('Тимин:', string.count('т'))

# 2
string1 = input()

adenine = string1.count('а') + string1.count('А')
guanine = string1.count('г') + string1.count('Г')
cytosine = string1.count('ц') + string1.count('Ц')
thymine = string1.count('т') + string1.count('Т')

print(f'Аденин: {adenine}')
print(f'Гуанин: {guanine}')
print(f'Цитозин: {cytosine}')
print(f'Тимин: {thymine}')

# 9.4.3
n = int(input())
string_count = 0

for i in range(n):
    string1 = input()
    eleven_count = string1.count('11')
    if eleven_count >= 3:
        string_count += 1

print(string_count)

# 9.4.4
# 1
s = input()
k = 0
for c in '1234567890':
    k += s.count(c)
print(k)

# 2
string1 = input()
digits = '0123456789'
count = 0

for c in string1:
    if c in digits:
        count += 1

print(count)

# 9.4.5
string1 = input()

if string1.endswith('.com') or string1.endswith('.ru'):
    print('YES')
else:
    print('NO')

# 9.4.6
string1 = input()
count = 0
char_count = ''

for char in string1:
    if string1.count(char) >= count:
        count = string1.count(char)
        char_count = char

print(char_count)

# 9.4.7
string1 = input()

if string1.count('f') == 1:
    print(string1.find('f'))
elif string1.count('f') > 1:
    print(string1.find('f'), string1.rfind('f'))
else:
    print('NO')

# 9.4.8
# 1
string1 = input()
index1 = string1.find('h')
index2 = string1.rfind('h')
print(string1.replace(string1[index1:index2 + 1], ''))

# 2
text = input()
print(text[:text.find("h")] + text[text.rfind("h") + 1:])
