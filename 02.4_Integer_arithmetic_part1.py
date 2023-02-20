# 2.4
# 2.4.1
num_1 = int(input())
num_2 = num_1 + 1
num_3 = num_2 + 1

print(num_1)
print(num_2)
print(num_3)
print()

# 2.4.2
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(num_1 + num_2 + num_3)
print()

# 2.4.3
a = int(input())
V = a ** 3  # Объем куба.
S = 6 * (a ** 2)  # Площадь куба.

print('Объем =', V)
print('Площадь полной поверхности =', S)
print()

# 2.4.4
a = int(input())
b = int(input())
function_1 = (3 * (a + b) ** 3) + (275 * b ** 2) - (127 * a) - 41

print(function_1)
print()

# 2.4.5
num = int(input())
num_prev = num - 1
num_next = num + 1

print(f'Следующее за числом {num} число: {num_next}')
print(f'Для числа {num} предыдущее число: {num_prev}')
print()

# 2.4.6
screen_cost = int(input())  # Стоимость монитора.
system_cost = int(input())  # Стоимость системного блока.
keyboard_cost = int(input())  # Стоимость клавиатуры.
mouse_cost = int(input())  # Стоимость мыши.

computer_cost = screen_cost + system_cost + keyboard_cost + mouse_cost  # Стоимость компьютера.

print(3 * computer_cost)
print()

# 2.4.7
num_1 = int(input())
num_2 = int(input())

print(f'{num_1} + {num_2} = {num_1 + num_2}')
print(f'{num_1} - {num_2} = {num_1 - num_2}')
print(f'{num_1} * {num_2} = {num_1 * num_2}')
print()

# 2.4.8
a_1 = int(input())
d = int(input())
n = int(input())

a = a_1 + d * (n - 1)

print(a)
print()

# 2.4.9
x = int(input())
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')
print()
