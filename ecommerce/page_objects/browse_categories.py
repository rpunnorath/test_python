import time

from selenium.webdriver.common.by import By

from ecommerce.page_objects.base_page import BasePage
from ecommerce.page_objects.testdata import TestData


class BrowseCategories(BasePage):
    """Home page for the e-commerce site"""

    #---Browse categories---
    browse_list = "div[id='block_top_menu']>ul"
    sub_category_women = "//*[@id='block_top_menu']/ul/li[1]/ul"
    sub_cat_dress = (By.XPATH,"//*[@id='block_top_menu']/ul/li[2]")
    sub_cat_dress_list =  "//*[@id='block_top_menu']/ul/li[2]/ul"
    t_shirts = (By.XPATH,"//*[@id='block_top_menu']/ul/li[3]")
    hover_women = (By.CSS_SELECTOR, "a[title='Women']")
    hover_dresses = (By.CSS_SELECTOR, "a[title='Dresses']")
    tshirts_page = (By.XPATH, "//*[@id='center_column']/h1/span[1]")

    #--search box--
    search_box = (By.ID, "search_query_top")
    butn_search= (By.NAME, "submit_search" )
    search_results_list = "div[class='ac_results']>ul"
    product_listing = (By.CSS_SELECTOR, "div[id='center_column']>h1")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.INDEX_PAGE_URL)

    def browse_categories_with_css(self,browse_list):
        """
        Method to return the list
        :param browse_list: The the <ul> CSS locator element
        """
        option_list =[]
        time.sleep(3)
        resultSet = self.driver.find_element_by_css_selector(browse_list)
        options = resultSet.find_elements_by_tag_name("li")
        for option in options:
            option_list.append(option.text)
        return option_list

    def browse_categories_with_xpath(self,browse_list):
        """
        Method to return the list of categories
        :param browse_list: The the <ul> XPATH locator element
        """
        option_list =[]
        resultSet = self.driver.find_element_by_xpath(browse_list)
        options = resultSet.find_elements_by_tag_name("li")
        for option in options:
            option_list.append(option.text)
        return option_list
