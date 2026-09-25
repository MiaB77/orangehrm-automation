from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PIMPage(BasePage):

    PIM_BUTTON = (By.CSS_SELECTOR, "a[href*='/web/index.php/pim/viewPimModule']")
    PIM_HEADER = (By.XPATH, "//h6[text()='PIM']")
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button') and contains(., 'Add')]")
    SEARCH_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button--secondary') and contains(., 'Search')]")
    EMPLOYEE_NAMES = (By.XPATH, "//div[@class='oxd-table-card']//div[@data-v-6c07a142]")
    EMPLOYEE_CHECKBOX = (By.XPATH, "//div[@class='oxd-table-card-cell-checkbox']//label")
    DELETE_EMPLOYEE_BUTTON = (By.XPATH, "//button[.//i[contains(@class,'bi-trash')]]")
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

    def get_search_results(self):
        self.wait_for_element(self.EMPLOYEE_NAMES)
        elements = self.driver.find_elements(*self.EMPLOYEE_NAMES)
        return [el.text.strip() for el in elements if el.text.strip()]

    def delete_employee(self):
        self.click(self.EMPLOYEE_CHECKBOX)
        self.click(self.DELETE_EMPLOYEE_BUTTON)
        self.click(self.YES_DELETE_BUTTON)