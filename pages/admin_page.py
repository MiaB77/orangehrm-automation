from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminPage(BasePage):
    ADMIN_BUTTON = (By.CSS_SELECTOR, "a[href*='/web/index.php/admin/viewAdminModule']")
    USERNAME_INPUT = (By.XPATH, "//div[@class='oxd-table-filter-area']//input")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button--secondary') and contains(.,'Search')]")
    RESULTS = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")
    TABLE_CELLS = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']//div[@role='cell']")

    def navigate_to_admin_page(self):
        self.click(self.ADMIN_BUTTON)

    def search_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def get_results(self):
        def stable_result(driver):
            matches = [el.text.strip() for el in driver.find_elements(*self.RESULTS) if "Record Found" in el.text]
            if matches and matches == stable_result.previous:
                return matches[0]
            stable_result.previous = matches
            return False

        stable_result.previous = None
        return self.wait.until(stable_result)

    def get_table_cells(self):
        def stable_cells(driver):
            texts = [el.text.strip() for el in driver.find_elements(*self.TABLE_CELLS) if el.text.strip()]
            if texts and texts == stable_cells.previous:
                return texts
            stable_cells.previous = texts
            return False

        stable_cells.previous = None
        return self.wait.until(stable_cells)
