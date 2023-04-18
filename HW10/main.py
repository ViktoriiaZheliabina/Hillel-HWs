# ДЗ 10. OOP principals: Abstaraction, Inheritance and Hiding. Потрібно описати будь-який транспортний засіб або
# гаджет(на вибір) , з кількома рівнями абстракції, використовуючи ті принципи ООП, що ми розглядали:
# наслідування абстракцію і приховування даних

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

        Returns: None

        """
        self.__passengers += people

    def get_passengers(self) -> int:
        """

        Returns: number of passengers onboard

        """
        return self.__passengers


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

        Returns: None

        """
        self.__cargo += weight

    def get_cargo(self) -> float:
        """

        Returns: cargo weight onboard in tons

        """
        return self.__cargo


class Liner(PassengerShip):
    """Describes a liner ship"""
    def __init__(self, name: str, seats: int, pools: int):
        """

        Args:
            name: ship's name
            seats: number of seats onboard
            pools: number of pools onboard
        """
        super().__init__(name, seats)
        self.pools = pools
        self.__cruise = []

    def get_type(self) -> str:
        """

        Returns: type of the ship

        """
        return "Liner"

    def __clean_pools(self) -> None:
        """Clean all pools

        Returns: None

        """
        pass

    def start_cruise(self, cruise: []) -> None:
        """Create cruise as a list of cities

        Args:
            cruise: List of city names

        Returns: None

        """
        self.__cruise = cruise
        self.__clean_pools()


class Tanker(CargoShip):
    """Describes a tanker ship"""
    def __init__(self, name: str, capacity: int, tanks: int):
        """

        Args:
            name: ship's name
            capacity: cargo capacity (tons)
            tanks: number of tanks onboard
        """
        super().__init__(name, capacity)
        self.tanks = tanks

    def get_type(self) -> str:
        """

        Returns: type of the ship

        """
        return "Tanker"

    def clean_tanks(self) -> None:
        """Clean tanks

        Returns: None

        """
        pass


if __name__ == '__main__':
    KnockNevis = Tanker("Knock Nevis", 564763, 8)
    KnockNevis.clean_tanks()
    KnockNevis.docking(14582.25)
    KnockNevis.docking(-2456.33)
    KnockNevis.docking(8854.6)
    print(f"{KnockNevis.get_type()} \"{KnockNevis.name}\" cargo: {KnockNevis.get_cargo()} tons")

    QueenMary2 = Liner("Queen Mary 2", 3090, 2)
    QueenMary2.book(254)
    QueenMary2.book(1065)
    QueenMary2.start_cruise(["London", "Barcelona", "Stambul", "Odessa"])
    print(f"{QueenMary2.get_type()} \"{QueenMary2.name}\" passengers: {QueenMary2.get_passengers()}")
