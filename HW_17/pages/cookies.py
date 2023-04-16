from selenium.webdriver import Chrome


class Cookies:
    """Describes Cookie"""
    def __init__(self, driver: Chrome):
        self.cookies = {}
        self.driver = driver

    def set_cookie(self, name, value) -> None:
        """Adds new cookies

        Args:
            name: cookie's name
            value: cookie's value

        Returns: Cookie

        """
        self.driver.add_cookie({"name": name, "value": value})

    def get_cookie(self, name) -> str:
        """Returns cookie

        Args:
            name: cookie's name

        Returns: Cookie

        """
        if name in self.cookies:
            return self.cookies[name]
        else:
            cookie = self.driver.get_cookie(name)
            if cookie:
                self.cookies[name] = cookie['value']
                return cookie['value']
            else:
                return "None"

    def clear_cookies(self) -> None:
        """Clears cookie

        Returns: None

        """
        self.cookies.clear()
        self.driver.delete_all_cookies()