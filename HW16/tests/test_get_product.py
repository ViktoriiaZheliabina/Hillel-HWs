
def test_get_product(categories):
    categories.choose_category("Мобильная связь")
    product_list = categories.choose_sub_category('Мобильные телефоны')
    item_page = product_list.choose_product()
    title = 'Мобильные телефоны — купить мобильные телефоны по лучшей цене в Украине, Киев, Харьков, Одесса, Днепр, Львов'
    assert item_page.get_title(title) == title
    categories.scroll()


