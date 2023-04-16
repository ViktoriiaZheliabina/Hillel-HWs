import pytest
from selenium.webdriver import Chrome

from HW_17.pages.categories.categories import Categories
from HW_17.pages.cookies import Cookies


@pytest.fixture(scope='session')
def driver():
    driver = Chrome("drivers/cromedriver")
    driver.maximize_window()

    driver.get("https://stylus.ua/")
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def categories(driver):
    yield Categories(driver)


@pytest.fixture(scope='session')
def cookies(driver):
    yield Cookies(driver)

