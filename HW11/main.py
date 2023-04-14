# ДЗ 11. OOP principals. Опишіть будь-який об'єкт, який має методи, що змінюють його стани.
# Треба реалізувати всі принципи ООП, що ми проходили.
# Але реалізацію не ускладнюйте, по 1-2 методи створіть.

from abc import ABC, abstractmethod


class Notebook(ABC):
    """Class that describe notebook object"""
    def __init__(self, model_name: str, cpu: str, ram: int, hdd: int, display: float, price: float):
        """

        Args:
            model_name:
            cpu:
            ram:
            hdd:
            display:
            price:
        """
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
        """
        Method that describes notebook model name
        :return
        model name: str
        """
        pass

    def get_characteristics(self):
        """
        Method gets notebook characteristics
        returns:
        list of characteristics: str
        """

        txt = f"{self.get_model_name()}\n"
        txt += f"  cpu: {self.cpu}\n"
        txt += f"  ram: {self.ram} Gb\n"
        if self.__is_hdd_present():
            txt += f"  HDD: {self.hdd} Gb\n"
        else:
            txt += "  HDD: none\n"
        txt += f"  display: {self.display}\"\n"
        txt += f"  price: {self.price} грн\n"
        return txt


class Sony(Notebook):
    """Class describes Sony model"""
    def __init__(self,  model_name: str, cpu: str, ram: int, hdd: int, display: float, price: float):
        super().__init__(model_name, cpu, ram, hdd, display, price)

    def get_model_name(self):
        return "Sony " + self.model_name


class Lenovo(Notebook):
    """Class describes Lenovo model"""
    def __init__(self, model_name: str, cpu: str, ram: int, hdd: int, ssd: int, display: float, price: float):
        super().__init__(model_name, cpu, ram, hdd, display, price)
        self.ssd = ssd

    def get_model_name(self):
        return "Lenovo " + self.model_name

    def get_characteristics(self):
        return super().get_characteristics() + f"  SSD: {self.ssd} Gb\n"


if __name__ == '__main__':
    sonyVaio = Sony("VAIO SVF1521A7EB", "Intel Pentium 2117U", ram=4, hdd=500, display=15.6, price=5480)
    lenovoIdeaPad3 = Lenovo("IdeaPad 3 15IAU7", "Intel Core i5-1235", ram=16, hdd=0, ssd=512, display=15.6, price=25999)

    print(sonyVaio.get_characteristics())
    print(lenovoIdeaPad3.get_characteristics())
