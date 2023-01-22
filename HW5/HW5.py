# Задача 5.
# Напишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:

# Попросіть користувача ввести свсвій вік.

# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!)
# - вивести "О, вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"

# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік

# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.

# Наприклад :

# "Тобі ж 5 років! Де твої батьки?"

# "Вам 81 рік? Покажіть пенсійне посвідчення!"

# "О, вам 33 роки! Який цікавий вік!"

# Після отримання відповіді програма повинна спитати користувача, чи
# хоче він повторити виконання. Користувач відповідає Yes або No.
# У випадку коли користувач відповів Yes програма повторюється, No - завершується.
# Користувач повинен мати змогу повторити виконання програми необмежену кількість разів.

# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг або тайпхінтінг.
# Не забувайте що кожна функція має виконувати тільки одне завдання і про правила написання коду.
# P.S. Для цієї і для всіх наступних домашок пишіть в функціях докстрінги або хінтінг

def func_inp():
    """ Введення віку. Повертає вік у вигляді string"""
    print('Enter your age, please:')
    return input()


def check_exit():
    """
    Перевірка на вихід із програми.
    :return: True - якщо користувач хоче вийти, False - якщо користувач бажає продовжити роботу з програмой.
    """
    while True:
        ans = input('Do you want to continue? (Yes/No): ')
        if ans.lower() == 'no':
            return True
        elif ans.lower() == 'yes':
            return False
        print ('Incorrect value')


def get_year_ending(age):
    """
    Повертає необхідне слово залежно від кількості років
    :param age: string
    :return: string
    """
    iage = int(age)
    if 10 < iage < 15:
        return 'років'
    last = int(age[-1])
    if last == 1:
        return 'рік'
    elif 1 < last < 5:
        return 'роки'
    else:
        return 'років'


while True:
    age = func_inp()
    if age.isdigit():
        iage = int(age)
        if iage > 9 and age[0] == age[1]:
            print(f'О, вам {age} {get_year_ending(age)}! Який цікавий вік!')
        elif iage < 7:
            print(f'Тобі ж {age} {get_year_ending(age)}! Де твої батьки?')
        elif iage < 16:
            print(f'Тобі лише {age} {get_year_ending(age)}, а це е фільм для дорослих!')
        elif iage > 65:
            print(f'Вам {age} {get_year_ending(age)}? Покажіть пенсійне посвідчення!')
        else:
            print(f'Незважаючи на те, що вам {age} {get_year_ending(age)}, білетів всеодно нема!')
    else:
        print('Incorrect value')

    if check_exit():
        break