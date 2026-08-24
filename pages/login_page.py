from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = BASE_URL

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "orangehrm-login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "oxd-alert--error")
    INVALID_CREDENTIALS_MESSAGE = (By.CSS_SELECTOR,"p.oxd-alert-content-text")


    def open(self):
        super().navigate_to(self.URL)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

