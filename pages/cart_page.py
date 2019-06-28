from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_be_empty_cart(self):
        empty_cart_message_element = self.driver.find_element(*CartPageLocators.EMPTY_CART_MESSAGE_BLOCK)
        empty_cart_message = empty_cart_message_element.text
        # print(empty_cart_message)
        empty_cart_text = "Your basket is empty. Continue shopping"
        assert empty_cart_message == empty_cart_text, "The cart is not empty"

    def should_not_be_present_product_in_cart(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_NAME_IN_CART), "The product is in the cart, but it" \
                                                                                    "shouldn't be there"





