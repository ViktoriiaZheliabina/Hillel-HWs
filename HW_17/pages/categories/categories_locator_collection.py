from selenium.webdriver.common.by import By

from HW_17.core.locator import Locator


class CategoriesLocatorCollection:
    """ Contains Locators  of Categories """

    def __init__(self):
        self.cookies_button = Locator(By.XPATH, "//button[@class='submit-button']")

    @staticmethod
    def get_category(name: str) -> Locator:
        """ Returns category

        Args:
            name: name of category

        Returns: category

        """
        return Locator(By.XPATH, f"(//a[@ title='{name}'])[last()]")

    @staticmethod
    def get_sub_category(name: str) -> Locator:
        """Return sub-category

        Args:
            name: name of sub-category

        Returns: sub-category

        """
        return Locator(By.XPATH, f"(//a[@title='{name}'])[2]")

    @staticmethod
    def get_title_name(title: str) -> Locator:
        """Returns title name

        Args:
            title: name of the title

        Returns:
            title

        """
        return Locator(By.XPATH, f"//title[contains(text(),'{title}')]")

