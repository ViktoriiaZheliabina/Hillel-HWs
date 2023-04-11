from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator: Tuple[By.XPATH, str]):
        element: WebElement = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def click(self, locator: Tuple[By.XPATH, str]):
        element: WebElement = self.wait_for_element(locator)
        element.click()

