import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.data_loader import load_admin_data, load_login_data

valid_credentials, _ = load_login_data()
data = load_admin_data()

@pytest.mark.parametrize("cred_username, cred_password", valid_credentials)
class TestAdminPage:

    def _login_and_navigate_to_admin_page(self, driver, cred_username, cred_password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(cred_username, cred_password)
        admin_page = AdminPage(driver)
        admin_page.navigate_to_admin_page()
        admin_page.search_username(data["username"])
        admin_page.click_search_button()
        return admin_page

    def test_search_by_username(self, driver, cred_username, cred_password):
        admin_page = self._login_and_navigate_to_admin_page(driver, cred_username, cred_password)

        result = admin_page.get_results()
        assert "Record" in result and "Found" in result


    def test_verify_user_role(self,driver, cred_username, cred_password):
        admin_page = self._login_and_navigate_to_admin_page(driver, cred_username, cred_password)

        cells = admin_page.get_table_cells()
        assert data["expected_role"] in cells

    def test_verify_user_status(self, driver, cred_username, cred_password):
        admin_page = self._login_and_navigate_to_admin_page(driver, cred_username, cred_password)

        cells = admin_page.get_table_cells()
        assert data["expected_status"] in cells