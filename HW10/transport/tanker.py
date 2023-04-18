from HW10.transport.cargoship import CargoShip


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
        """Clean tanks"""
        pass