from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.driver.current_url
        assert "login" in url

        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        email_login_field = self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD)
        password_login_field = self.driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD)
        forgot_password_login_link = self.driver.find_element(*LoginPageLocators.LOGIN_FORGOT_PASSWORD_LINK)
        login_submit_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        assert (email_login_field.is_displayed() and password_login_field.is_displayed() and
                forgot_password_login_link.is_displayed() and login_submit_button.is_displayed())

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        email_registration_field = self.driver.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        password_registration_field = self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        confirm_password_registration_field = (self.driver.find_element
                                               (*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD))
        registration_submit_button = self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        assert (email_registration_field.is_displayed() and password_registration_field.is_displayed() and
                confirm_password_registration_field.is_displayed() and registration_submit_button.is_displayed())