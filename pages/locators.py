from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL_FIELD = (By.NAME, "login-username")
    LOGIN_PASSWORD_FIELD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    LOGIN_FORGOT_PASSWORD_LINK = (By.PARTIAL_LINK_TEXT, "password-reset")
    REGISTRATION_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.NAME, "registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration-submit")