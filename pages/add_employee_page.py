from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddEmployeePage(BasePage):

    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='Last Name']")

    SAVE_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button') and contains(., 'Save')]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'p.oxd-text--toast-message')

    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.LAST_NAME_INPUT, last_name)

    def click_save_button(self):
        self.click(self.SAVE_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)



