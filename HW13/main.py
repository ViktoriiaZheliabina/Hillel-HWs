# ДЗ 13. OOP patterns: Singletone, Factory method
# Створити клас Shop:
# клас має містити метод, що створює об'єкт товару(гречка, печиво, яблуко)
# всі товари мають батьківський клас Item, що є абстрактним класом
# PS. Не на оцінку, якщо цікаво, спробуйте змінити в нашому декораторі сінглтон
# поле інстанс - зробити його приватним

from buckwheat import Buckwheat
from cake import Cake
from apple import Apple


class Shop:
    """Class describes behavior of object Shop"""

    items = []

    def __init__(self, name: str):
        """
        Args:
        name: shop's name
        """
        self.name = name

    @staticmethod
    def create_item(item: str, name: str, price: float, expired_date: str):
        """Method creates an item

        Args:
            item: type of item
            name: item's name
            price: item's price
            expired_date: item's expire date

        Returns: created item

        """
        if item == "buckwheat":
            return Buckwheat(name, price, expired_date)
        elif item == "cake":
            return Cake(name, price, expired_date)
        elif item == "apple":
            return Apple(name, price, expired_date)
        else:
            raise Exception("Incorrect item name")


if __name__ == "__main__":

    shop = Shop("Viktoria")

    shop.items.append(Shop.create_item("buckwheat", "Hutorock", 100, "02.01.2025"))
    shop.items.append(Shop.create_item("cake", "Roshen", 180, "02.01.2025"))
    shop.items.append(Shop.create_item("apple", "Golden", 50, "02.05.2023"))

    for i in shop.items:
        print(i.desc())
