from typing import Tuple


class Locator:
    """
    Describes locator object
    """
    def __init__(self, method: str, query: str):
        """

        Args:
            method: XPATH or CSS
            query: XPATH (CSS) query
        """
        self.__method = method
        self.__query = query

    def to_tuple(self) -> Tuple[str, str]:
        """ Converts to Tuple

        Returns: Tuple

        """
        return self.__method, self.__query
