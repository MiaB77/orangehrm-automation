from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

        DASHBOARD_HEADER = (By.CLASS_NAME, "oxd-topbar-header-breadcrumb-module")

        def is_dashboard_displayed(self):
            return self.is_element_displayed(self.DASHBOARD_HEADER)