from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_1():
    driver = Chrome("drivers/cromedriver")
    driver.maximize_window()
    driver.get("https://rozetka.com.ua/ua/")
    search_locator = "//input[@placeholder='Я шукаю...']"
    first_find_element = "//ul[@class='suggest-list']/li[4]"
    desired_item = "//ul[@class='catalog-grid ng-star-inserted']/li[8]"
    search_input: WebElement = driver.find_element(By.XPATH, search_locator)
    search_input.send_keys("Ноутбук")
    sleep(1)
    second_result: WebElement = driver.find_element(By.XPATH, first_find_element)
    second_result.click()
    sleep(1)
    item_result: WebElement = driver.find_element(By.XPATH, desired_item)
    item_result.click()
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)
    driver.quit()





