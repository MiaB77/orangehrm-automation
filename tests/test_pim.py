import pytest
from pages.login_page import LoginPage
from pages.PIM_page import PIMPage
from pages.add_employee_page import AddEmployeePage
from utils.data_loader import load_login_data, load_employee_data

valid_credentials, _ = load_login_data()
employees = load_employee_data()

@pytest.mark.parametrize("username, password", valid_credentials)
@pytest.mark.parametrize("first_name, last_name", employees)

class TestPIM:

    def _login_and_navigate_to_pim(self, driver, username, password):
        login_page = LoginPage(driver)
        pim_page = PIMPage(driver)
        login_page.open()
        login_page.login(username, password)
        pim_page.navigate_to_pim()
        return pim_page

    @pytest.mark.order(1)
    def test_add_employee(self, driver, username, password, first_name, last_name):
        pim_page = self._login_and_navigate_to_pim(driver, username, password)

        pim_page.click_add_employee()

        add_employee_page = AddEmployeePage(driver)
        add_employee_page.enter_first_name(first_name)
        add_employee_page.enter_last_name(last_name)
        add_employee_page.click_save_button()

        success_message = add_employee_page.get_success_message()
        assert "Successfully Saved" in success_message, f"Error! Successfull pop-up didn't appear.Text found: {success_message} "

    @pytest.mark.order(2)
    def test_search_employee(self, driver, username, password, first_name, last_name):
        pim_page = self._login_and_navigate_to_pim(driver, username, password)

        pim_page.search_employee(f"{first_name} {last_name}")
        result = pim_page.get_search_results()
        assert any(first_name in name for name in result)


    @pytest.mark.order(3)
    def test_delete_employee(self, driver, username, password, first_name, last_name):
        pim_page = self._login_and_navigate_to_pim(driver, username, password)

        pim_page.search_employee(f"{first_name} {last_name}")
        pim_page.delete_employee()

        pim_page.search_employee(f"{first_name} {last_name}")
        result = pim_page.get_search_results()
        assert result == [], f"Employee {first_name} {last_name} still found after deletion: {result}"









