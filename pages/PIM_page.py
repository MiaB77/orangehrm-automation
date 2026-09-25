from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class PIMPage(BasePage):

    PIM_BUTTON = (By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewPimModule']")
    PIM_HEADER = (By.XPATH, "//h6[text()='PIM']")
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button') and contains(., 'Add')]")
    SEARCH_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button--secondary') and contains(., 'Search')]")
    TABLE_BODY = (By.XPATH, "//div[contains(@class,'oxd-table-body')]")
    EMPLOYEE_ROWS = (By.XPATH, "//div[contains(@class,'oxd-table-card')]")
    YES_DELETE_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button--label-danger') and contains(., 'Yes, Delete')]")


    def navigate_to_pim(self):
        self.click(self.PIM_BUTTON)

    def is_pim_displayed(self):
        return self.is_element_displayed(self.PIM_HEADER)

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

    def search_employee(self, name):
        self.enter_text(self.SEARCH_NAME_INPUT, name)
        self.click(self.SEARCH_BUTTON)
        self.wait_for_element(self.TABLE_BODY)

    def get_search_results(self):
        def read_rows(driver):
            try:
                rows = driver.find_elements(*self.EMPLOYEE_ROWS)
                texts = [row.text.strip() for row in rows if row.text.strip()]
                return texts or [""]
            except StaleElementReferenceException:
                return False

        return [text for text in WebDriverWait(self.driver, 10).until(read_rows) if text]

    def delete_employee(self, name):
        first_name, last_name = name.split(" ", 1)
        row_locator = (
            By.XPATH,
            "//div[contains(@class,'oxd-table-card')]"
            f"[.//*[normalize-space()={self._xpath_literal(first_name)}]]"
            f"[.//*[normalize-space()={self._xpath_literal(last_name)}]]",
        )
        row = self.wait_for_element(row_locator)
        row.find_element(By.XPATH, ".//div[contains(@class,'oxd-table-card-cell-checkbox')]//label").click()
        row.find_element(By.XPATH, ".//button[.//i[contains(@class,'bi-trash')]]").click()
        self.click(self.YES_DELETE_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.staleness_of(row))

    @staticmethod
    def _xpath_literal(value):
        if "'" not in value:
            return f"'{value}'"
        if '"' not in value:
            return f'"{value}"'
        parts = value.split("'")
        return "concat(" + ", \"'\", ".join(f"'{part}'" for part in parts) + ")"