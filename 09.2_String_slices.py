# 9.2
# 9.2.1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

# 9.2.2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

# 9.2.3
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

# 9.2.4
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# 9.2.5
# 1
string1 = input()

if string1 == string1[::-1]:
    print('YES')
else:
    print('NO')

# 2
string1 = input()

if string1[:len(string1) // 2] == string1[:-len(string1) // 2:-1]:
    print('YES')
else:
    print('NO')

# 9.2.6
string1 = input()

print(len(string1))
print(string1 * 3)
print(string1[0])
print(string1[:3])
print(string1[-3:])
print(string1[::-1])
print(string1[1:-1])

# 9.2.7
string1 = input()

print(string1[2])
print(string1[-2])
print(string1[:5])
print(string1[:-2])
print(string1[::2])
print(string1[1::2])
print(string1[::-1])
print(string1[-1::-2])

# 9.2.8
string1 = input()
mid_symbol = len(string1) // 2 + len(string1) % 2

result = string1[mid_symbol:] + string1[:mid_symbol]

print(result)
