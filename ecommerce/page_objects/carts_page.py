import time

from selenium.webdriver.common.by import By
from ecommerce.page_objects.base_page import BasePage


class CartPage(BasePage):
    """Cart Page on ecommerce site"""

    #--cart summary tab--
    carts_title = (By.XPATH, "//*[@id='cart_title']")
    checkout_tab_summary = (By.CSS_SELECTOR,"li[class='step_current  first']")
    add_quantity = (By.CSS_SELECTOR,"i[class='icon-plus']")
    cart_count_element = (By.CSS_SELECTOR,"input[class~='cart_quantity_input']")
    delete_quantity = (By.CSS_SELECTOR,"i[class='icon-minus']")
    proceed_checkout_button = (By.CSS_SELECTOR,"a[class~='standard-checkout']")
    alert_warning = (By.CSS_SELECTOR,"p[class='alert alert-warning']")
    checkout_tab_sign_in = (By.CSS_SELECTOR,"li[class='step_current second']")
    shipping_tab = (By.CSS_SELECTOR,"li[class='step_current four']")
    payment_tab = (By.CSS_SELECTOR,"li[class='step_current last']")

    #--address tab--
    address_tab = (By.CSS_SELECTOR,"li[class='step_current third']")
    address_delivery = (By.XPATH,"//*[@id='address_delivery'/li[1]/h3")
    address_billing = (By.XPATH,".//*[@id='address_invoice']/li[1]/h3")
    address_delivery_list = "ul[class='address item box']"
    address_shipping_list = "ul[class='address alternate_item box']"
    process_addr_butn1 = "processAddress"
    process_addr_butn =  (By.CSS_SELECTOR,"button[class='button btn btn-default button-medium']")

    #--hovered over popup cart--
    view_cart = (By.CSS_SELECTOR, "a[title='View my shopping cart']")
    butn_order_cart = (By.ID, "button_order_cart")

    #--delivery--
    #delivery_radio = "delivery_option_393725_0"
    delivery_radio = "div[class='radio']>span>input"
    terms_condtn_check = "cgv"
    process_carrier_butn = (By.NAME, "processCarrier")

    #--payment--
    payment_type_bank_wire = (By.CSS_SELECTOR,"a[class='bankwire']")
    confirm_order_button = (By.CSS_SELECTOR,"p[id='cart_navigation']>button")
    order_complete_msg= (By.CSS_SELECTOR,"p[class='cheque-indent']")

    def __init__(self, driver):
        super().__init__(driver)

    #method to return cart count
    def cart_count(self):
        int(self.driver.find_element(self.cart_count_element).text)

    #Empty cart msg
    def empty_alert(self):
        self.driver.find_element(self.alert_warning).text

    #method to delete quantity
    def delete_item(self):
        print("Cart Count is"+ str(self.cart_count))
        if (self.cart_count < 1):
            assert self.empty_alert == "Your shopping cart is empty."
        else:
            self.click(self.delete_quantity)

    #method to increase quantity
    def add_item(self):
        self.click(self.add_quantity)

    #method to proceed checkout
    def click_proceed_to_checkout_button(self):
        self.click(self.proceed_checkout_button)
        time.sleep(3)

    #mehotd to return the address list
    def get_address_list(self, addr_list):
        option_list =[]
        time.sleep(3)
        resultSet = self.driver.find_element_by_css_selector(addr_list)
        options = resultSet.find_elements_by_tag_name("li")
        for option in options:
            option_list.append(option.text)
        return option_list

    #method to check for cart summary page
    def cart_summary_page_check(self):
        time.sleep(10)
        assert self.is_visible(self.carts_title) is True
        assert self.is_visible(self.checkout_tab_summary) is True

        #verifies that the + sign to increase count works
        self.click(self.add_quantity)
        # verifies that the - sign to delete count works
        self.click(self.delete_quantity)

        self.click_proceed_to_checkout_button()

    #method to hover over cart and checkout
    def checkout_from_popup_cart(self):
        self.hover_to(self.view_cart)
        time.sleep(2)
        self.click(self.butn_order_cart)

    #method to process address and continue
    def click_process_address_button(self):
        self.driver.find_element_by_name(self.process_addr_butn1).click()
        time.sleep(10)

    #method to process carrier and continue
    def click_process_carrier_button(self):
        self.click(self.process_carrier_butn)

    #method to check if radio button for shipping is selected
    def is_shipping_selected(self):
        time.sleep(10)
        checked = self.driver.find_element_by_css_selector(self.delivery_radio).get_attribute("checked")
        if checked == 'true':
            return True
        else:
            return False

    #method to check  terms and condition
    def terms_and_condition_click(self):
        self.driver.find_element_by_name(self.terms_condtn_check).click()
        time.sleep(3)

    #method to confirm the order and click
    def click_confirm_order(self):
        self.click(self.confirm_order_button)