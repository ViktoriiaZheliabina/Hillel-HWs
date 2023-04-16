from selenium.webdriver import Chrome

from HW_17.pages.base_page import BasePage
from HW_17.pages.categories.categories_locator_collection import CategoriesLocatorCollection
from HW_17.pages.product_list import ProductList


class Categories(BasePage):
    """Describes categories in the page"""
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self.__locator_collection = CategoriesLocatorCollection()

    def choose_category(self, name: str) -> None:
        """Chooses the category by name

        Args:
            name: name of category

        Returns: None

        """
        self.click(self.__locator_collection.cookies_button)
        self.click(self.__locator_collection.get_category(name))

    def choose_sub_category(self, name: str) -> ProductList:
        """Chooses the sub-category by name

        Args:
            name:name of subcategory

        Returns: Product list

        """
        self.click(self.__locator_collection.get_sub_category(name))
        return ProductList(self.driver)





