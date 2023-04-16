class Employee:
    """Class describes object Employee"""
    def __init__(self, name: str, surname: str, age: int):
        """

        Args:
            name: Employee's name
            surname: Employee's surname
            age: Employee's age
        """
        self.name = name
        self.surname = surname
        self.age = age

    def get_name(self) -> str:
        """Method returns object's name

        Returns: Object's name

        """
        return self.name

    def get_surname(self) -> str:
        """Method returns object's surname

        Returns: Object's surname

        """

        return self.surname

    def get_age(self) -> int:
        """Method returns object's age

        Returns: Object's age

        """
        return self.age
