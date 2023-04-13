import pytest
from selenium.webdriver import Chrome
from HW16.pages.categories import Categories



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
