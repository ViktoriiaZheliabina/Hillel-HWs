from abc import ABC, abstractmethod


class Item(ABC):
    """Class describes behavior of the object Item"""

    def __init__(self, name: str, price: float, expired_date: str):
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
    def get_type(self) -> str:
        """Method returns item type

        Returns: item type
        """
        pass

    def desc(self) -> str:
        """Method returns description of item

        Returns: description
        """
        return f"{self.get_type()} \"{self.name}\": {self.price} UAH, expired: {self.expired_date}"


