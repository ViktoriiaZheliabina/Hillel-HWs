import pytest
from selenium.webdriver import Chrome

from HW16.pages.categories import Categories
from time import sleep


@pytest.fixture(scope='session')
def driver():
    driver = Chrome("drivers/cromedriver")
    driver.maximize_window()

    driver.get("https://rozetka.com.ua/ua/")
    sleep(1)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def categories(driver):
    yield Categories(driver)
