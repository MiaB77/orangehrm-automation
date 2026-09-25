from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):
    ADMIN_BUTTON = (By.CSS_SELECTOR, "a[href*='/web/index.php/admin/viewAdminModule']")
    USERNAME_INPUT = (By.XPATH, "//div[@class='oxd-table-filter-area']//input")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button--secondary') and contains(.,'Search')]")
    RESULTS = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")
    TABLE_CELLS = (By.XPATH, "//div[@class='oxd-table-body']//div[@data-v-6c07a142]")

    def navigate_to_admin_page(self):
        self.click(self.ADMIN_BUTTON)

    def search_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def get_results(self):
        return self.get_text(self.RESULTS)

    def get_table_cells(self):
        self.wait_for_element(self.TABLE_CELLS)
        elements = self.driver.find_elements(*self.TABLE_CELLS)
        return [el.text.strip() for el in elements if el.text.strip()]
