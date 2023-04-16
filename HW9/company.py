class Company:
    """Class describes Company object"""
    branches = []

    def __init__(self, name: str, type: str, number_of_employees: int):
        """
        Args:
            name: Company's name
            type: Company's type
            number_of_employees: Number of employees
        """
        self.name = name
        self.type = type
        self.number_of_employees = number_of_employees

    def get_name(self) -> str:
        """Method returns company's name

        Returns: Company's name

        """
        return self.name

    def get_type(self) -> str:
        """Method returns company's type (product, outsource, outstuff etc)

        Returns: Company's type

        """
        return self.type

    def get_number_of_employees(self) -> int:
        """Method returns the number of employees

        Returns: Number of employees

        """
        return self.number_of_employees

    def set_number_of_employees(self, number_of_employees: int) -> int:
        """Method sets the number of employees

        Args:
            number_of_employees: The set number of employees

        Returns: New number of employees

        """
        self.number_of_employees = number_of_employees
        return number_of_employees

    @classmethod
    def add_branches(cls, branch: str) -> None:
        """Method sets the name of Company's branch

        Args:
            branch: name of the branch

        Returns: None

        """
        cls.branches.append(branch)




