# ДЗ 11. OOP principals. Опишіть будь-який об'єкт, який має методи, що змінюють його стани.
# Треба реалізувати всі принципи ООП, що ми проходили.
# Але реалізацію не ускладнюйте, по 1-2 методи створіть.

from abc import ABC, abstractmethod


class Notebook(ABC):
    """Class that describe notebook object"""
    def __init__(self, model_name: str, cpu: str, ram: int, hdd: int, display: float, price: float):
        self.model_name = model_name
        self.cpu = cpu
        self.ram = ram
        if hdd < 0:
            self.hdd = 0
        else:
            self.hdd = hdd
        self.display = display
        self.price = price

    def __is_hdd_present(self):
        """Method returns True if hdd is present"""
        return self.hdd > 0

    @abstractmethod
    def get_model_name(self):
        """Method that describes notebook model"""
        pass

    def print_characteristics(self):
        """Method prints notebook charactristics"""
        print(self.get_model_name())
        print(f"  cpu: {self.cpu}")
        print(f"  ram: {self.ram} Gb")
        if self.__is_hdd_present():
            print(f"  HDD: {self.hdd} Gb")
        else:
            print(f"  HDD: none")
        print(f"  display: {self.display}\"")
        print(f"  price: {self.price} грн")


class SSD:
    """Class describes SSD"""
    def __init__(self, size):
        self.__size = size

    def get_ssd_size(self):
        """Method returns SSD size"""
        if self.__size < 0:
            return 0
        else:
            return self.__size


class Sony(Notebook):
    """Class describes Sony model"""
    def __init__(self, model_name: str, cpu: str, ram: int, hdd: int, display: float, price: float):
        super().__init__(model_name, cpu, ram, hdd, display, price)

    def get_model_name(self):
        return "Sony " + self.model_name


class Lenovo(Notebook, SSD):
    """Class describes Lenovo model"""
    def __init__(self, model_name: str, cpu: str, ram: int, hdd: int, ssd: int, display: float, price: float):
        Notebook.__init__(self, model_name, cpu, ram, hdd, display, price)
        SSD.__init__(self, ssd)

    def get_model_name(self):
        return "Lenovo " + self.model_name

    def print_characteristics(self):
        Notebook.print_characteristics(self)
        print(f"  SSD: {SSD.get_ssd_size(self)}")


def get_model_name(self):
    return "  Lenovo " + self.model_name


if __name__ == '__main__':
    lenovoIdeaPad3 = Lenovo("IdeaPad 3 15IAU7", "Intel Core i5-1235U", ram=16, hdd=0, ssd=512, display=15.6, price=25999)
    sonyVaio = Sony("VAIO SVF1521A7EB", "Intel Pentium 2117U", ram=4, hdd=500, display=15.6, price=5480)

    lenovoIdeaPad3.print_characteristics()
    print()
    sonyVaio.print_characteristics()
