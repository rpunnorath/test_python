from selenium.webdriver.common.by import By
from ecommerce.page_objects.base_page import BasePage

class ProductDetailsPage(BasePage):
    """Product Details Page for the clicked product"""

    # --product details--
    printed_summer_dress = (By.XPATH, "//*[@id='center_column']/ul/li[1]/div/div[1]/div/a[1]")
    printed_summer_dress_more = (By.XPATH, "//*[@id='center_column']/ul/li[1]/div/div[2]/div[2]/a[2]/span")
    butn_twitter = (By.CSS_SELECTOR, "button[class~='btn-twitter']")
    butn_fb = (By.CSS_SELECTOR, "button[class~='btn-facebook']")
    butn_gplus = (By.CSS_SELECTOR, "button[class~='btn-google-plus']")
    butn_pintrst = (By.CSS_SELECTOR, "button[class~='btn-pinterest']")
    add_to_cart = (By.CSS_SELECTOR, "#add_to_cart > button")

    # --cart details
    shopping_cart = (By.CSS_SELECTOR, "a[href='http://automationpractice.com/index.php?controller=order']")
    checkout_link = (By.XPATH, "//*[@id='button_order_cart']/span/text()")
    proceed_checkout = (By.CSS_SELECTOR, "a[title='Proceed to checkout']")
    popup = (By.ID, "layer_cart")

    def __init__(self,driver):
        super().__init__(driver)

    #Method to click on add to cart button
    def click_add_to_cart_button(self):
        self.click(self.add_to_cart)

    #Method to click on procedd checkout button
    def click_proceed_to_checkout_button(self):
        self.click(self.proceed_checkout)
