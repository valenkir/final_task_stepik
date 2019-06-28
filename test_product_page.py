import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage


def test_guest_cant_see_success_message(driver): #should pass
    product_link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(driver, product_link)
    page.open()
    page.should_not_display_success_message()


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                #  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                #  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                #  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                #  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                 # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(driver):
    product_link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(driver, product_link)
    page.open()
    page.add_product_to_cart()


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_not_be_present_product_in_cart()
