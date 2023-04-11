from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from typing import Tuple
from HW16.pages.base_page import BasePage


class Categories(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

    def choose_category(self, name: str):
        category_locator: Tuple[By.XPATH, str] = (By.XPATH, f"/a[@role='button'][contains(text(),'{name}')]")
        self.click(category_locator)


