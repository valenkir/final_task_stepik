from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_name_element = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_price_text = product_price.text
        product_name_text = product_name_element.text
        # print(product_price.text)
        # print(product_name.text)
        add_to_cart_button.click()
        # self.solve_quiz_and_get_code()
        self.should_be_corresponding_product_name(product_name_text)
        self.should_be_corresponding_product_price(product_price_text)

    def should_be_corresponding_product_name(self, product_name):
        product_name_element_in_success_message = self.driver.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE)
        product_name_in_success_message = product_name_element_in_success_message.text
        print(product_name_in_success_message)
        assert product_name_in_success_message == product_name, ("Product name in the cart is not equal to the "
                                                                      "name of the product selected on the product page")

    def should_be_corresponding_product_price(self, product_price):
        product_price_element_in_success_message = self.driver.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_SUCCESS_MESSAGE)
        product_price_in_success_message = product_price_element_in_success_message.text
        print(product_price_in_success_message)
        assert product_price_in_success_message == product_price, ("Product price in the cart is not equal to the "
                                                                      "price of the product selected on the product "
                                                                        "page")

    def should_not_display_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_SUCCESS_MESSAGE) and self\
            .is_not_element_present(*ProductPageLocators.PRODUCT_OFFER_SUCCESS_MESSAGE) and self.\
            is_not_element_present(*ProductPageLocators.PRODUCT_PRICE_SUCCESS_MESSAGE), "Success message is displayed," \
                                                                                       "but shouldn't"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_SUCCESS_MESSAGE) and self\
            .is_disappeared(*ProductPageLocators.PRODUCT_OFFER_SUCCESS_MESSAGE) and self.\
            is_disappeared(*ProductPageLocators.PRODUCT_PRICE_SUCCESS_MESSAGE), "Success message is displayed, " \
                                                                               "but shouldn't"

