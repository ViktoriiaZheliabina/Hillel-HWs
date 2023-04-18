from abc import abstractmethod

from HW10.transport.ship import Ship


class CargoShip(Ship):
    """Describes cargo ship object"""
    def __init__(self, name: str, capacity: float):
        """

        Args:
            name: ship's name
            capacity: cargo capacity (tons)
        """
        super().__init__(name)
        self.capacity = capacity
        self.__cargo = 0.

    @abstractmethod
    def get_type(self) -> str:
        """

        Returns: type of the ship

        """
        pass

    def docking(self, weight: float) -> None:
        """Load / unload cargo in the dock

        Args:
            weight: weight of the cargo to load/unload (negative value - unload)

        """
        self.__cargo += weight

    def get_cargo(self) -> float:
        """

        Returns: cargo weight onboard in tons

        """
        return self.__cargo