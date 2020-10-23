import pytest

from ecommerce.page_objects.login_page import LoginPage
from ecommerce.page_objects.testdata import TestData


@pytest.mark.usefixtures("chrome_driver_init")
class TestLoginPositive:
    """ This is the Login and account creation page tests """

    def test_create_account(self):
        """Create an account using the required items"""
        login_page = LoginPage(self.driver)
        login_page.enter_text(login_page.create_account, TestData.new_email)
        login_page.click(login_page.account_create_button)
        login_page.assert_element_text(login_page.account_create_title, "CREATE AN ACCOUNT")
        login_page.enter_text(login_page.first_name, TestData.first_name)
        login_page.enter_text(login_page.last_name, TestData.last_name)
        login_page.enter_text(login_page.password_field, TestData.password)
        login_page.enter_text(login_page.addr_first_name, TestData.first_name)
        login_page.enter_text(login_page.addr_last_name, TestData.last_name)
        login_page.enter_text(login_page.address, TestData.address)
        login_page.enter_text(login_page.city, TestData.city)
        login_page.select_item("id_state", TestData.state)
        login_page.enter_text(login_page.postcode, TestData.postcode)
        login_page.select_item("id_country", TestData.country)
        login_page.enter_text(login_page.mobile_phone, TestData.mobile_phone)
        login_page.enter_text(login_page.alias, TestData.alias)
        login_page.click(login_page.submit_acct_buttn)
        login_page.assert_element_text(login_page.account_created_title, "MY ACCOUNT")
        login_page.click(login_page.logout)

    def test_login_with_cred(self):
        """Login with the created credentials"""
        login_page = LoginPage(self.driver)
        login_page.login_with_cred(TestData.email, TestData.password)
        login_page.assert_element_text(login_page.account_created_title, "MY ACCOUNT")

@pytest.mark.usefixtures("chrome_driver_init")
class TestLoginNegative:
    """ Tests to verify the negative scenarios for login and create account """

    def test_create_account_with_invalid_email(self):
        """Create an account with invalid values"""
        login_page = LoginPage(self.driver)
        login_page.enter_text(login_page.create_account, TestData.invalid_email)
        login_page.click(login_page.account_create_button)
        assert login_page.is_visible(login_page.invalid_email_error) is True

    #parametrize the test to verify the invalid emaail error
    @pytest.mark.parametrize("email,password", TestData.invalid_email_set)
    def test_sign_in_with_invalid_email(self, email, password):
        """Login with an invalid email"""
        login_page = LoginPage(self.driver)
        login_page.enter_text(login_page.email_field, email)
        login_page.enter_text(login_page.password_field, password)
        login_page.click(login_page.sign_in_button)
        assert login_page.is_visible(login_page.sign_in_invalid_email_error) is True
