# 11.7
"""

Общий вид списочного выражения следующий:
[выражение for переменная in последовательность],
где переменная — имя некоторой переменной, последовательность — последовательность значений,
которые она принимает (список, строка или объект, полученный при помощи функции range),
выражение — некоторое выражение, как правило, зависящее от использованной в списочном выражении переменной,
которым будут заполнены элементы списка.

1. Создать список, заполненный 10 нулями можно и при помощи списочного выражения:
zeros = [0 for i in range(10)]

2. Создать список, заполненный квадратами целых чисел от 0 до 9 можно так:
squares = [i ** 2 for i in range(10)]

3. Создать список, заполненный кубами целых чисел от 10 до 20 можно так:
cubes = [i ** 3 for i in range(10, 21)]

4. Создать список, заполненный символами строки:
chars = [c for c in 'abcdefg']

5. Считать количество строк, а затем заполнить список строками:
lines = [input() for _ in range(int(input()))]

6. Считать количество чисел, а затем заполнить список числами:
numbers = [int(input()) for _ in range(int(input()))]

Списочное выражение             Результирующий список
[0 for i in range(10)]          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[i ** 2 for i in range(1, 8)]   [1, 4, 9, 16, 25, 36, 49]
[i * 10 for i in numbers]       [10, 140, 50, 90, 120]
[c * 2 for c in word]           ['HH', 'ee', 'll', 'll', 'oo']
[m[0] for m in words]           ['o', 't', 't', 'f', 'f', 's']
[i for i in numbers if i < 10]  [1, 5, 9]
[m[0] for m in words if len(m) == 3]    ['o', 't', 's']

"""
# 11.7.1
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [s[1:] for s in keywords]

print(new_keywords)

# 11.7.2
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [len(s) for s in keywords]

print(lengths)

# 11.7.3
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
            'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
            'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [s for s in keywords if len(s) >= 5]

print(new_keywords)

# 11.7.4
palindromes = [i for i in range(100, 1001) if str(i)[0] == str(i)[-1]]

print(palindromes)

# 11.7.5
numbers = [i ** 2 for i in range(1, int(input()) + 1)]
for n in numbers:
    print(n)

# 11.7.6
numbers = [int(i) ** 3 for i in input().split()]
for n in numbers:
    print(n, end=' ')

# 11.7.7
[print(s) for s in input().split()]

# 11.7.8
print(*[char for char in input() if char.isdigit()], sep='')

# 11.7.9
list_squares = [int(i) ** 2 for i in input().split() if (int(i) % 2 == 0) and ((int(i) ** 2) % 10 != 4)]
print(*list_squares)
