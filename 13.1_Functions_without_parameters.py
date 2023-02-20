# 13.1
# 13.1.1
def draw_box():
    print('*' * 10)
    for _ in range(12):
        print('*        *')
    print('*' * 10)


draw_box()

# 13.1.2
def draw_box():
    for i in range(1, 11):
        print('*' * i)


draw_box()
