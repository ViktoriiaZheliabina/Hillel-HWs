from typing import Tuple

from selenium.webdriver.common.by import By

from HW_17.core.locator import Locator
from HW_17.pages.base_page import BasePage
from HW_17.pages.product import Product


class ProductList(BasePage):
    """ Describes list of products"""
    def __init__(self, driver):
        super().__init__(driver)
        self.__first_entry_locator: Locator = Locator(By.XPATH, "(//div[@class='name-block'])[1]")

    def choose_product(self):
        """Chooses first element

        Returns: Product

        """
        self.click(self.__first_entry_locator)
        return Product(self.driver)
