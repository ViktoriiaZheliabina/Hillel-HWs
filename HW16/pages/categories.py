from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from typing import Tuple
from HW16.pages.base_page import BasePage
from HW16.pages.product_list import ProductList


class Categories(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

    def choose_category(self, name: str):
        category_locator: Tuple[By.XPATH, str] = (By.XPATH, f"(//a[@ title='{name}'])[last()]")
        self.click(category_locator)

    def choose_sub_category(self, name: str):
        sub_category_locator: Tuple[By.XPATH, str] = (By.XPATH, f"(//a[@title='{name}'])[2]")
        self.click(sub_category_locator)
        return ProductList(self.driver)





