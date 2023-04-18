from HW10.transport.passengership import PassengerShip


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
        """Clean all pools"""
        pass

    def start_cruise(self, cruise: []) -> None:
        """Create cruise as a list of cities

        Args:
            cruise: List of city names

        """
        self.__cruise = cruise
        self.__clean_pools()