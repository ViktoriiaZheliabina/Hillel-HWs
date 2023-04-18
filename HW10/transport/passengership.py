from abc import abstractmethod

from HW10.transport.ship import Ship


class PassengerShip(Ship):
    """Describes passenger ship object"""
    def __init__(self, name: str, seats: int):
        """

        Args:
            name: ship's name
            seats: number of seats
        """
        super().__init__(name)
        self.seats = seats
        self.__passengers = 0

    @abstractmethod
    def get_type(self) -> str:
        """

        Returns: type of the ship

        """
        pass

    def book(self, people: int) -> None:
        """Booking seats

        Args:
            people: number of seats to book. Can be negative or positive

        """
        self.__passengers += people

    def get_passengers(self) -> int:
        """

        Returns: number of passengers onboard

        """
        return self.__passengers