import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.data_loader import load_login_data

valid_credentials, invalid_credentials = load_login_data()

class TestLogin:
    @pytest.mark.parametrize("username, password", valid_credentials)
    def test_valid_login(self, driver, username, password):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        login_page.open()
        login_page.login(username, password)

        assert dashboard_page.is_dashboard_displayed()

    @pytest.mark.parametrize("username, password", invalid_credentials)
    def test_invalid_login(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)
        error = login_page.get_error_message()
        assert error == "Invalid credentials"




