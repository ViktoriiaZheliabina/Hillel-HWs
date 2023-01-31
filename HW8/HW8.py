# 1. Напишіть функцію, яка на вхід буде приймати список стрінгів, а в результаті повертати
# список в якому всі стрінги будуть у верхньому регістрі. Використати для цього функцію map()
# Наприклад на вхід: ['alfred', 'ben', 'william']
# а на вихід: ['ALFRED', 'BEN', 'WILLIAM']


def upper_foo(list_low):
    list_upper = list(map(lambda x: x.upper(), list_low))
    return list_upper


print(upper_foo(['alfred', 'ben', 'william']))


# 2. Напишіть функцію, яка на вхід буде приймати список флоатів, а в результаті
# повертати список в якому всі числа будуть піднесені в степінь 2 і заокруглені до
# трьох знаків після коми.
# Використати для цього функцію map()
# Наприклад на вхід: [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# а на вихід: [18.922, 37.088, 10.562, 95.453, 4.666, 78.854, 21.068]

def degree_foo(list_input):
    list_degree = list(map(lambda x: round(x**2), list_input))
    return list_degree


print(degree_foo([4.35, 6.99, 3.25, 9.77, 2.16, 8.88, 4.59]))


# 3. Напишіть функцію, яка на вхід буде приймати два списки, а в результаті повертати список
# в якому попарно об'єднані в тупли елементи.
# Використати для цього функцію zip()
# Наприклад на вхід: ['a', 'b', 'c', 'd', 'e'], [1,2,3,4,5]
# а на вихід: [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

def union_to_tuple(list_input1, list_input2):
    list_tuple = dict(zip(list_input1, list_input2))
    return list_tuple


print(union_to_tuple(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5]))


# 4. Напишіть функцію, яка на вхід буде приймати список стрінгів і число,
# а в результаті повертати список в якому будуть ті стрінги, довжина яких буде менша за число
# Використати для цього функцію filter()
# Наприклад на вхід: ["Jeff", "Alex", "Jonathan", "Richelle", "Anna"], 5
# а на вихід: ["Jeff", "Alex", "Anna"]


def list_string_less_num(list_inp, num):
    list_out = list(filter(lambda k: len(k) < num, list_inp))
    return list_out


print(list_string_less_num(["Jeff", "Alex", "Jonn", "Richelle", "Anna"], 5))


