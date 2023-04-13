from typing import Tuple

from selenium.webdriver.common.by import By
from HW16.pages.base_page import BasePage
from HW16.pages.product import Product


class ProductList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__first_entry_locator: Tuple[By.XPATH, str] = (By.XPATH, "(//div[@class='name-block'])[1]")

    def choose_product(self):
        self.click(self.__first_entry_locator)
        return Product(self.driver)
