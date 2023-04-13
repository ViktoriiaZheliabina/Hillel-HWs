from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Describes base methods of the page"""
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator: Tuple[By.XPATH, str]):
        """Waits for element to be present"""
        element: WebElement = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def click(self, locator: Tuple[By.XPATH, str]):
        """Clicks the element"""
        element: WebElement = self.wait_for_element(locator)
        element.click()

    def scroll(self):
        """Scrolls down the page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


