# 14 Test
import math

# 14.1
def draw_triangle():
    star = 1
    space = 7
    for i in range(8):
        print((' ' * space) + ('*' * star), sep='')
        star = star + 2
        space = space - 1


draw_triangle()

# 14.2
# 1
def get_shipping_cost(quantity):
    remainder = quantity - 1

    if remainder > 0:
        result = 1000 + remainder * 120
    else:
        result = 1000

    return result


number_of_goods = int(input())

print(get_shipping_cost(number_of_goods))

# 2
def get_shipping_cost(quantity):
    cost = 1000
    for i in range(quantity - 1):
        cost = cost + 120
    return cost


n = int(input())

print(get_shipping_cost(n))

# 14.3
def compute_binom(n, k):
    binom = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return int(binom)


n, k = int(input()), int(input())

print(compute_binom(n, k))

# 14.4
def number_to_list(num):
    num_list = []

    while num != 0:
        num_list.append(int(num % 10))
        num = num // 10
    num_list.reverse()

    return num_list


def number_to_words(num):
    numbers1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    numbers2 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
                'восемнадцать', 'девятнадцать']
    numbers3 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if 1 <= num <= 10:
        result = numbers1[num - 1]

    if 11 <= num <= 19:
        result = numbers2[num - 11]

    if 20 <= num <= 99:
        num_list = number_to_list(num)
        if num_list[1] == 0:
            result = numbers3[num_list[0] - 2]
        else:
            result = numbers3[num_list[0] - 2] + ' ' + numbers1[num_list[1] - 1]

    return result


number = int(input())

print(number_to_words(number))

# 14.5
def get_month(language, number):
    months_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    months_en =  ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    if language == 'ru':
        result = months_ru[number - 1]
    if language == 'en':
        result = months_en[number - 1]

    return result


lan = input()
num = int(input())

print(get_month(lan, num))

# 14.6
def is_magic(date):
    date_list = date.split('.')

    if int(date_list[0]) * int(date_list[1]) == int(date_list[2][2:]):
        return True
    else:
        return False


date = input()

print(is_magic(date))

# 14.6
def is_pangram(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    flag = True

    for char in alphabet:
        if char not in text:
            flag = False
            break

    return flag


text = input()

print(is_pangram(text))
