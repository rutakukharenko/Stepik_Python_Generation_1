# 9.1
# 9.1.1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])

# 9.1.2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[39])

# 9.1.3
string1 = input()

for i in range(0, len(string1), 2):
    print(string1[i])

# 9.1.4
string1 = input()

for i in range(len(string1) - 1, -1, -1):
    print(string1[i])

# 9.1.5
name = input()
surname = input()
patronymic = input()

print(surname[0] + name[0] + patronymic[0])

# 9.1.6
string1 = input()
sum = 0

for c in string1:
    sum = sum + int(c)

print(sum)

# 9.1.7
string1 = input()
digits = '0123456789'
flag = False

for c in string1:
    if c in digits:
        flag = True
        break

if flag:
    print('Цифра')
else:
    print('Цифр нет')

# 9.1.8
string1 = input()
count1 = 0
count2 = 0

for c in string1:
    if c == '+':
        count1 += 1
    if c == '*':
        count2 += 1

print(f'Символ + встречается {count1} раз')
print(f'Символ * встречается {count2} раз')

# 9.1.9
string1 = input()
count = 0

for i in range(len(string1) - 1):
    if string1[i] == string1[i + 1]:
        count += 1

print(count)

# 9.1.10
string1 = input()
vowels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
vowels_count = 0
consonants_count = 0

for c in string1:
    if c in vowels:
        vowels_count += 1
    if c in consonants:
        consonants_count += 1

print(f'Количество гласных букв равно {vowels_count}')
print(f'Количество согласных букв равно {consonants_count}')

# 9.1.11
# 1
n = int(input())
binary = ''

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print(binary)

# 2
string_bin = bin(int(input()))
print(string_bin[2::])

