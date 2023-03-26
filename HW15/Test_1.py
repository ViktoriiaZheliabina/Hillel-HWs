from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_1():
    driver = Chrome("drivers/cromedriver")
    driver.maximize_window()
    driver.get("https://rozetka.com.ua/ua/")
    search_locator = "//input[@placeholder='Я шукаю...']"
    first_find_element = "//span[normalize-space()='microsoft']"
    desired_item = "//span[contains(text(),'Ноутбук Microsoft Surface Laptop (Model 1769) Coba')]"
    search_input: WebElement = driver.find_element(By.XPATH, search_locator)
    search_input.send_keys("Ноутбук")
    sleep(1)
    second_result: WebElement = driver.find_element(By.XPATH, first_find_element)
    second_result.click()
    sleep(2)
    item_result: WebElement = driver.find_element(By.XPATH,desired_item)
    item_result.click()
    sleep(1)
    driver.quit()





