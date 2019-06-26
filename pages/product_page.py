from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()


