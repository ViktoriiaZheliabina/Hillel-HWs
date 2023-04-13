from selenium.webdriver.common.by import By
from HW16.pages.base_page import BasePage


class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self, title):
        self.wait_for_element((By.XPATH, f"//title[contains(text(),'{title}')]"))
        return self.driver.title


