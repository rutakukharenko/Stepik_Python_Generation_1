# 11.1
# 11.1.1
n = int(input())
numbers = list(range(1, n + 1))
print(numbers)

# 11.1.2
# 1
n = int(input())
symbols_ascii = list(range(ord('a'), ord('a') + n))
symbols = []

for num in symbols_ascii:
    symbols.append(chr(num).lower())

print(symbols)

# 2
n = int(input())
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
print(abc[0:n])
