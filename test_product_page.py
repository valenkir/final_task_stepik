from .pages.product_page import ProductPage

def test_guest_can_add_product_to_cart():
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(driver, product_link)
    page.open()
    page.add_product_to_cart()
    # page.should_be_success_message()
