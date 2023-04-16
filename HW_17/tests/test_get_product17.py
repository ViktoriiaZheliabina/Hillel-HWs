from time import sleep


def test_get_product(categories):
    categories.choose_category("Мобильная связь")
    product_list = categories.choose_sub_category('Мобильные телефоны')
    item_page = product_list.choose_product()
    sleep(1)
    title = 'Мобильные телефоны — купить мобильные телефоны по лучшей цене в Украине, Киев, Харьков, Одесса, Днепр, Львов'
    assert item_page.get_title(title) == title


def test_cookies(cookies):
    cookies.set_cookie("qwerty", "12345")
    cookie_added = cookies.get_cookie("qwerty")
    assert cookie_added == "12345"


def test_cookies_clear(cookies):
    cookies.clear_cookies()
    cookie_found = cookies.get_cookie("")
    assert cookie_found == "None"


