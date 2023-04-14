from item import Item


class Cake(Item):
    """Describes Cake"""

    def __init__(self, name: str, price: float, expired_date: str):
        """

        Args:
            name: item's name
            price: item's price
            expired_date: item's expire date
        """
        super().__init__(name, price, expired_date)

    def get_type(self) -> str:
        """Method returns item type

        Returns: item type
        """
        return "Cake"
