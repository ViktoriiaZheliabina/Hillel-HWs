from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from HW_17.core.locator import Locator
from HW_17.pages.cookies import Cookies


class BasePage:
    """Describes base methods of the page"""

    def __init__(self, driver: Chrome):
        self.cookie = Cookies(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator: Locator):
        """
        Waits for element to be present
        Args:
            locator: locator

        Returns: element

        """
        element: WebElement = self.wait.until(EC.presence_of_element_located(locator.to_tuple()))
        return element

    def click(self, locator: Locator):
        """Clicks the element

        Args:
            locator: locator

        Returns: element

        """
        element: WebElement = self.wait_for_element(locator)
        element.click()




