# 6.2
# 6.2.1
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."
string1 = '"Python is a great language!", '
string2 = 'said Fred. '
string3 = '''"I don"t ever remember having this much fun before."'''
result = string1 + string2 + string3
print(result)

# 6.2.2
name, surname = input(), input()
print(f'Hello {name} {surname}! You just delved into Python')

# 6.2.3
football_team = input()
print(f'Футбольная команда {football_team} имеет длину {len(football_team)} символов')

# 6.2.4
city_1, city_2, city_3 = input(), input(), input()
len_city_1, len_city_2, len_city_3 = len(city_1), len(city_2), len(city_3)

max_len = max(len_city_1, len_city_2, len_city_3)
min_len = min(len_city_1, len_city_2, len_city_3)

if min_len == len_city_1:
    print(city_1)
elif min_len == len_city_2:
    print(city_2)
elif min_len == len_city_3:
    print(city_3)

if max_len == len_city_1:
    print(city_1)
elif max_len == len_city_2:
    print(city_2)
elif max_len == len_city_3:
    print(city_3)

# 6.2.5
string1, string2, string3 = input(), input(), input()
len_string1, len_string2, len_string3 = len(string1), len(string2), len(string3)

max_len = max(len(string1), len(string2), len(string3))
min_len = min(len(string1), len(string2), len(string3))
mid_len = (len_string1 + len_string2 + len_string3) - (max_len + min_len)

if (mid_len - min_len) == (max_len - mid_len):
    print('YES')
else:
    print('NO')

# 6.2.6
string1 = input()
string2 = 'синий'

if string2 in string1:
    print('YES')
else:
    print('NO')

# 6.2.7
string1 = input()
string2 = 'суббота'
string3 = 'воскресенье'

if (string2 in string1) or (string3 in string1):
    print('YES')
else:
    print('NO')

# 6.2.8
email = input()
if ('@' in email) and ('.' in email):
    print('YES')
else:
    print('NO')
