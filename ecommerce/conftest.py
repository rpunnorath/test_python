import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ecommerce.page_objects.login_page import LoginPage


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver= driver
    yield
    driver.close()
    driver.quit()


@pytest.mark.usefixtures("chrome_driver_init")
@pytest.fixture()
def login_with_credential(request,username,password):
    page = LoginPage(request.cls.driver)
    page.login_with_cred(username,password)
    yield
    logging.debug("Credential Login")
    page.logout()
