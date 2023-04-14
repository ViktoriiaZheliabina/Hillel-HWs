# ДЗ 11. OOP principals. Опишіть будь-який об'єкт, який має методи, що змінюють його стани.
# Треба реалізувати всі принципи ООП, що ми проходили.
# Але реалізацію не ускладнюйте, по 1-2 методи створіть.

from abc import ABC, abstractmethod


class Notebook(ABC):
    """Class describes notebook object"""
    def __init__(self, model_name: str = "unknown", cpu: str = "unknown", ram: int = 0, hdd: int = 0, display: float = 0, price: float = 0):
        """

        Args:
            model_name: Notebook model name
            cpu: CPU name
            ram: RAM size
            hdd: HDD size
            display: Display diagonal
            price: Price in UAH


        """
        self.model_name = model_name
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.display = display
        self.price = price

    def __get_hdd_desc(self) -> str:
        """ Method returns HDD description

        Returns: HDD description

        """
        if self.hdd > 0:
            return f"HDD: {self.hdd} Gb\n"
        else:
            return "HDD: none\n"

    @abstractmethod
    def get_model_name(self) -> str:
        """Method returns notebook model name

        Returns: Notebook model name

        """
        pass

    def get_characteristics(self) -> str:
        """Method returns list of characteristics

        Returns: List of characteristics

        """
        txt = f"{self.get_model_name()}\n  cpu: {self.cpu}\n  ram: {self.ram} Gb\n  {self.__get_hdd_desc()}  display: {self.display}\"\n  price: {self.price} грн\n"
        return txt


class Sony(Notebook):
    """Class describes Sony model"""
    def __init__(self,  model_name: str, cpu: str, ram: int, hdd: int, display: float, price: float):
        """

        Args:
            model_name: Sony notebook model name
            cpu: CPU name
            ram: RAM size
            hdd: HDD size
            display: Display diagonal
            price: Price in UAH
        """
        super().__init__(model_name, cpu, ram, hdd, display, price)

    def get_model_name(self) -> str:
        """Method returns Sony notebook model name

        Returns:  Sony notebook model name

        """
        return "Sony " + self.model_name


class Lenovo(Notebook):
    """Class describes Lenovo model"""
    def __init__(self, model_name: str, cpu: str, ram: int, hdd: int, ssd: int, display: float, price: float):
        """

        Args:
            model_name: Lenovo notebook model name
            cpu: CPU name
            ram: RAM size
            hdd: HDD size
            display: Display diagonal
            price: Price in UAH
        """
        super().__init__(model_name, cpu, ram, hdd, display, price)
        self.ssd = ssd

    def get_model_name(self) -> str:
        """Method returns Lenovo notebook model name

        Returns: Lenovo notebook model name

        """
        return "Lenovo " + self.model_name

    def get_characteristics(self) -> str:
        """Method returns list of characteristics

        Returns: List of characteristics

        """
        return super().get_characteristics() + f"  SSD: {self.ssd} Gb\n"


if __name__ == '__main__':
    sonyVaio = Sony("VAIO SVF1521A7EB", "Intel Pentium 2117U", ram=4, hdd=500, display=15.6, price=5480)
    lenovoIdeaPad3 = Lenovo("IdeaPad 3 15IAU7", "Intel Core i5-1235", ram=16, hdd=0, ssd=512, display=15.6, price=25999)

    print(sonyVaio.get_characteristics())
    print(lenovoIdeaPad3.get_characteristics())
