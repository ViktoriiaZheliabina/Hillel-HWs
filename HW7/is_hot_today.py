def is_hot_today(temp=30):
    return temp > 25


def input_temperature():
    while True:
        t = input("Веедите число:")
        if t.isdigit():
            return int(t)
        else:
            print("Wrong!!!")


if is_hot_today(input_temperature()):
    print('жарко')
else:
    print('холодно')