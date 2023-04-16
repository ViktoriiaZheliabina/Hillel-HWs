from selenium.webdriver.common.by import By

from HW_17.pages.base_page import BasePage
from HW_17.pages.categories.categories_locator_collection import CategoriesLocatorCollection


class Product(BasePage):
    """ Describes product's base methods"""
    def __init__(self, driver):
        super().__init__(driver)
        self.__locator_collection = CategoriesLocatorCollection()

    def get_title(self, title: str) -> str:
        """ Return page's title name

        Args:
            title: Title of the page

        Returns:
            name of the title

        """
        self.wait_for_element(self.__locator_collection.get_title_name(title))
        return self.driver.title


