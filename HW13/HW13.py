#Створити клас Shop:
#клас має містити метод, що створює об'єкт товару(гречка, печиво, яблуко)
#всі товари мають батьківський клас Item, що є абстрактним класом

# PS. Не на оцінку, якщо цікаво, спробуйте змінити в нашому декораторі сінглтон
# поле інстанс - зробити його приватним

from abc import ABC, abstractmethod


class Item:
    """Class describes behavior of object Item"""
    def __init__(self, name: str, price:int, expired_date: str):
        """
        Args:
         name: item's name
         price: item's price
         expired_date: item's expire date
        """
        self.name = name
        self.price = price
        self.expired_date = expired_date

    @abstractmethod
    """Method describes the possibility to sell/buy items"""
    def sell_buy(self):
        pass


class Grecha(Item):
    def sell_buy(self):
        pass


class Cake(Item):
    def sell_buy(self):
        pass


class Apple(Item):
    def sell_buy(self):
        pass


class Shop:
    """Class describes behavior of object Shop"""

    items = []

    def __init__(self, name: str):
        """
        Args:
        name: shop's name
        """
        self.name = name

    @classmethod
    def add_item(cls, item: Item):
        """Method creates item"""
        return cls.items.append(item)


# Перевірка роботи коду

if __name__ == "__main__":
    our_shop = Shop("Vika")
    our_shop.add_item(Grecha("Xutorock", 100, "02.01.2025"))
    our_shop.add_item(Cake("Roshen", 180, "02.01.2025"))
    our_shop.add_item(Apple("Golden", 50, "02.05.2023"))
    print("end")



