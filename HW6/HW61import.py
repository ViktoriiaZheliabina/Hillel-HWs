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
        print('Incorrect value')


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


def measure_time(func):
    """Вимірює і виводить на екран час виконання функції в секундах"""
    def wrapper():
        import time
        start = time.time()
        func()
        end = time.time()
        print('Час виконання: {} секунд.'.format(end-start))
    return wrapper


@measure_time
def kassir_main():
    """ Виводить на екран повідомлення залежно від попередньо введеного віку"""
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