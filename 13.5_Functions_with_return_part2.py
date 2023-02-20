# 13.5
# 13.5.1
def is_valid_triangle(side1, side2, side3):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))

# 13.5.2
def is_prime(num):
    flag = True
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag


n = int(input())

print(is_prime(n))

# 13.5.3
def get_next_prime(num):
    n = num + 1
    while True:  # Есть граница, выше которой не надо.
        # Запускаем перебор для проверки на делимость.
        for i in range(2, n):  # От единицы до нашего числа включительно!
            if n % i == 0:  # Если нет остатка, то есть, число делится на что-то.
                n += 1  # Добавляем единицу.
                break  # Прерываем цикл.
        else:  # Дошли до конца цикла.
            return n  # Значит, наше число простое.


n = int(input())

print(get_next_prime(n))

# 13.5.4
def is_password_good(password):
    a = (len(password) > 7)
    b = (password != password.lower())
    c = (password != password.upper())
    d = not password.isalpha()
    return a and b and c and d


txt = input()

print(is_password_good(txt))

# 13.5.5
def is_one_away(word1, word2):
    count = 0
    flag = True

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
    else:
        flag = False

    if count == 1:
        flag = True
    else:
        flag = False

    return flag


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))

# 13.5.6
def is_palindrome(text):
    text_list = [char.lower() for char in text if char.isalpha()]
    text = ''.join(text_list)
    reversed_text = ''.join(reversed(text_list))

    if text == reversed_text:
        return True
    else:
        return False


txt = input()

print(is_palindrome(txt))

# 13.5.7
def is_palindrome(text):
    reversed_text = ''.join(reversed(text))

    if text == reversed_text:
        return True
    else:
        return False


def is_prime(num):
    flag = True
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_valid_password(password):
    password_list = password.split(':')
    flag = True
    flag1 = True
    flag2 = True
    flag3 = True

    if len(password_list) == 3:
        flag1 = is_palindrome(password_list[0])
        flag2 = is_prime(int(password_list[1]))
        flag3 = is_even(int(password_list[2]))
    else:
        flag = False

    return flag and flag1 and flag2 and flag3


password = input()

print(is_valid_password(password))

# 13.5.8
def is_correct_bracket(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    # Возвращаем True, если text с пустой строкой.
    return not text


txt = input()

print(is_correct_bracket(txt))

# 13.5.9
def convert_to_python_case(text):
    result = ''

    for i in range(len(text)):
        if text[i].isupper() and i !=0:
            result = result + '_' + text[i]
        else:
            result = result + text[i]

    result = result.lower()
    return result


text = input()

print(convert_to_python_case(text))