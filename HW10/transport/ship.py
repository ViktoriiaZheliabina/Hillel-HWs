from abc import ABC, abstractmethod


class Ship(ABC):
    """Describes a ship object"""
    def __init__(self, name: str):
        """

        Args:
            name: ship's name

        """
        self.name = name

    @abstractmethod
    def get_type(self) -> str:
        """

        Returns: type of the ship

        """
        pass