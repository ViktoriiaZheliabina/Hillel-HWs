# ДЗ 12. OOP: Functor, Iterator.
# 1.Створити клас Action, що повинен містити передану при ініціалізації "Дію".
# Створити клас Human, для якого в конструкторі ініціалізувати "Дію" і створити для неї приватне поле action.
# Написати проперті, що поверне "Дію".
# Створити список з об'єктів класу Human.
# Перебрати цей список і викликати action, як функцію.

import CustomIterator


class Action:
    """Class that contains Action"""
    def __init__(self, action):
        self.action = action

    def __call__(self, *args, **kwargs):
        """
        Get human's info
        Returns:
             human info: str
        """
        info = self.action(*args, **kwargs)
        return f"Name: {info['name']},  age: {info['age']}"


class Human:
    """Class that describe Human object"""

    def __init__(self, name: str, age: int):
        """

        :param name: human's name
        :param age: huma's age
        """
        self.name = name
        self.age = age
        self.__action = Action(self.get_info)

    @property
    def action(self):
        """Returns action"""
        return self.__action

    def get_info(self):
        """
        Get human's info
        Returns:
        human's name and age: dict
        """
        return {"name": self.name,  "age": self.age}


if __name__ == '__main__':
    humans = [Human("Paul", 21),
              Human("Iren", 13),
              Human("Bob", 14),
              Human("Nick", 44),
              Human("Mary", 16),
              Human("Ahmed", 115)]

    for i in humans:
        print(i.action())

    print("CustomIterator(humans, 0, 5):")
    for i in CustomIterator.CustomIterator(humans, 0, 5):
        print(i.action())

    print("CustomIterator(humans, 1, 3):")
    for i in CustomIterator.CustomIterator(humans, 1, 3):
        print(i.action())

    print("CustomIterator(humans, 2, 2):")
    for i in CustomIterator.CustomIterator(humans, 2, 2):
        print(i.action())

