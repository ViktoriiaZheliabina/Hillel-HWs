# Завдання 1.
# Створіть клас з описом будь-якої компанії. Наприклад Hillel, Epam, Google.
# Так як ми робили з людиною, тобто клас Company, що буде універсальним.

# Створіть клас з описом будь-якого працівника(Типу універсальний). Employee.

# Поки немає необхідності зв'язувати перший і другий класи.

# Намагайтесь максимально повно описати класи на предмет полів і методів.
# Додайте анотації до всіх методів. До кожного метода обов'язково треба додати док стрінгу
# з описом метода і анотації.

class Company:
    """Клас що описує об'єкт Company"""
    branches = []

    def __init__(self, name: str, type: str, number_of_employees: int = None):
        """

        :param name: назва  об'єкт Company
        :param type: тип діяльності, що веде  об'єкт Company
        :param number_of_employees: кількість працівнків в  об'єкт Company
        """
        self.name = name
        self.type = type
        self.number_of_employees = number_of_employees

    def get_name(self):
        """Метод повертає ім'я об'єкту із класу Company"""
        return self.name

    def get_type(self):
        """Метод повертає тип (product, outsource, outstuff etc) об'єкту із класу Company"""
        return self.type

    def get_number_of_employees(self):
        """Метод повертає кількість співробітників об'єкту із класу Company"""
        return self.number_of_employees

    def add_number_of_employees(self, number_of_employees):
        """Метод дозволяє задати кількість співробітників об'єкту із класу Company"""
        self.number_of_employees = number_of_employees

    @classmethod
    def add_branches(cls, branch: str):
        """Метод задає назву відділення об'єкту із класу Company"""
        return cls.branches.append(branch)


class Employee:
    """Клас що описує об'єкт Employee"""
    def __init__(self, name: str, surname: str, age: int):
        """

        :param name: ім'я об'єкт Employee
        :param surname: прізвище об'єкт Employee
        :param age: вік об'єкт Employee
        """
        self.name = name
        self.surname = surname
        self.age = age

    def get_name(self):
        """Метод повертає ім'я об'єкту із класу Employee"""
        return self.name

    def get_surname(self):
        """Метод повертає прізвище об'єкту із класу Employee"""
        return self.surname

    def get_age(self):
        """Метод повертає вік об'єкту із класу Employee"""
        return self.age

