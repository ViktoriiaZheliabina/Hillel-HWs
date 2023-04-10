# ДЗ 12. OOP: Functor, Iterator. 1.Створити клас Action, що повинен містити передану при ініціалізації "Дію".
#
# Створити клас Human, для якого в конструкторі ініціалізувати "Дію" і створити для неї приватне поле action.
# Написати проперті, що поверне "Дію".
# Створити список з об'єктів класу Human.
# Перебрати цей список і викликати action, як функцію.

class Action:
    """Class that contains Action"""
    def __init__(self, action):
        self.action = action

    def __call__(self, *args, **kwargs):
        self.action(*args, **kwargs)


class Human:
    """Class that describe Human object"""

    def __init__(self, name: str, age: int):
        """

        :param name: human's name
        :param age: huma's age
        """
        self.name = name
        self.age = age
        self.__action = Action(self.print_info)

    def get_action(self):
        return self.__action

    def print_info(self):
        print(f"Name: {self.name},  age: {self.age}");

    action = property(get_action)


if __name__ == '__main__':
    humans = [Human("Саша", 21),
              Human("Ира", 13),
              Human("Толя", 14),
              Human("Коля", 44),
              Human("Валя", 16),
              Human("Ахмед", 115)]

    for i in humans:
        i.action()
    print()

    # 2.Створити ітератор, що прийме послідовність і буде перебирати значення в заданому діапазоні.
    # CustomIterator(sequence, start_index, end_index)

    class CustomIterator:
        """Class that accepts a sequence and iterates through the values in the given range"""
        def __init__(self, sequence: list, start_index: int, end_index: int):
            if start_index < 0 or start_index >= len(sequence):
                raise BaseException("стартовый индекс выходит за пределы последовательности")
            if start_index > end_index:
                raise BaseException("стартовый индекс больше конечного")
            if end_index < 0 or end_index >= len(sequence):
                raise BaseException("конечный иддекс выходит за пределы последовательности")
            self.sequence = sequence
            self.start_index = start_index
            self.end_index = end_index
            self.position = start_index

        def __iter__(self):
            return self

        def __next__(self):
            if self.position <= self.end_index:
                item = self.sequence[self.position]
                self.position += 1
                return item
            else:
                raise StopIteration


    for i in CustomIterator(humans, 0, 5):
        i.action()
    print()

    for i in CustomIterator(humans, 1, 3):
        i.action()
    print()

    for i in CustomIterator(humans, 2, 2):
        i.action()

