import time

from selenium.webdriver.common.by import By

from ecommerce.page_objects.base_page import BasePage
from ecommerce.page_objects.testdata import TestData


class LoginPage(BasePage):
    """Login page for the ecommerce site"""

    # --- Home Page Sign in Locators ---
    email_field = (By.ID, "email")
    password_field = (By.ID, "passwd")
    sign_in_button = (By.ID, "SubmitLogin")

    # ---Account creation----
    create_account = (By.ID, "email_create")
    account_create_button = (By.NAME, "SubmitCreate")
    account_create_title = (By.CSS_SELECTOR, "div[id='noSlide']>h1")

    # ---Personal information---
    first_name = (By.ID, "customer_firstname")
    last_name = (By.ID, "customer_lastname")
    addr_first_name = (By.ID, "firstname")
    addr_last_name = (By.ID, "lastname")
    address = (By.ID, "address1")
    city = (By.ID, "city")
    postcode = (By.ID, "postcode")
    mobile_phone = (By.ID, "phone_mobile")
    alias = (By.ID, "alias")
    submit_acct_buttn = (By.ID, "submitAccount")
    account_created_title = (By.CSS_SELECTOR, "div[id='center_column']>h1")
    logout = (By.CSS_SELECTOR, "a[class='logout']")
    invalid_email_error = (By.ID, "create_account_error")
    sign_in_invalid_email_error = (By.CSS_SELECTOR,"div[class~='alert-danger']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login_with_cred(self, email, password):
        """ Method to login with credentials
        :param email: The email field value
        :param password: The password field value
        """
        self.enter_text(self.email_field, email)
        self.enter_text(self.password_field, password)
        self.click(self.sign_in_button)
        time.sleep(10)