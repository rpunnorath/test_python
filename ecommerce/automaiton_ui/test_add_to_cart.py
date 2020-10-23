import time
import pytest

from ecommerce.page_objects.browse_categories import BrowseCategories
from ecommerce.page_objects.carts_page import CartPage
from ecommerce.page_objects.login_page import LoginPage
from ecommerce.page_objects.product_details import ProductDetailsPage
from ecommerce.page_objects.testdata import TestData


@pytest.mark.usefixtures("chrome_driver_init")
class TestAddcart:
    """Add items to cart    """
    def test_add_item_to_cart(self):
        """Search and add an item to cart and checkout"""

        browse_page = BrowseCategories(self.driver)
        browse_page.enter_text(browse_page.search_box, "dresses")
        browse_page.click(browse_page.butn_search)
        product_page= ProductDetailsPage(self.driver)
        product_page.hover_to(product_page.printed_summer_dress)
        time.sleep(10)
        product_page.click(product_page.printed_summer_dress_more)
        assert product_page.is_visible(product_page.butn_twitter) is True
        assert product_page.is_visible(product_page.butn_fb) is True
        assert product_page.is_visible(product_page.butn_gplus) is True
        assert product_page.is_visible(product_page.butn_pintrst) is True
        product_page.click_add_to_cart_button()
        time.sleep(10)
        product_page.click_proceed_to_checkout_button()
        carts_page = CartPage(self.driver)
        carts_page.cart_summary_page_check()
        assert carts_page.is_visible(carts_page.checkout_tab_sign_in) is True
        time.sleep(3)

        #Login to the account before checkout
        page = LoginPage(self.driver)
        page.login_with_cred(TestData.email, TestData.password)
        page.assert_element_text(page.account_created_title, "MY ACCOUNT")

        #go to cart and checkout
        carts_page = CartPage(self.driver)
        carts_page.checkout_from_popup_cart()
        carts_page.cart_summary_page_check()
        assert carts_page.is_visible(carts_page.address_tab) is True
        del_list = carts_page.get_address_list(carts_page.address_delivery_list)
        #verifies the delivery address
        assert (all (item in del_list for item in (TestData.address_list)))
        #verifies the billing address
        ship_list = carts_page.get_address_list(carts_page.address_shipping_list)
        assert (all(item in ship_list for item in (TestData.ship_list)))
        carts_page.click_process_address_button()
        assert carts_page.is_visible(carts_page.shipping_tab) is True
        assert carts_page.is_shipping_selected() is True
        carts_page.terms_and_condition_click()
        carts_page.click_process_carrier_button()
        assert carts_page.is_visible(carts_page.payment_tab) is True
        carts_page.click(carts_page.payment_type_bank_wire)
        #confirm payment and checkout
        carts_page.click_confirm_order()
        assert carts_page.is_visible(carts_page.order_complete_msg) is True
