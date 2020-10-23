import time

import pytest

from ecommerce.page_objects.browse_categories import BrowseCategories
from ecommerce.page_objects.testdata import TestData


@pytest.mark.usefixtures("chrome_driver_init")
class TestBrowseCategories:
    """Browsing the store’s main categories (Women, Dresses, T-shirts)
        Searching for clothing items
    """
    def test_browse_categories(self):
        """Browsing the index page categories-Women,Dresses,T-shirts"""

        browse_page = BrowseCategories(self.driver)
        options = browse_page.browse_categories_with_css(browse_page.browse_list)
        assert (all(item in options for item in ("WOMEN", "DRESSES", "T-SHIRTS")))
        browse_page.hover_to(browse_page.hover_women)
        time.sleep(2)
        sub_options = browse_page.browse_categories_with_xpath(browse_page.sub_category_women)
        assert (any(item in sub_options for item in (TestData.browse_categories)))
        browse_page.click(browse_page.hover_women)
        browse_page.hover_to(browse_page.sub_cat_dress)
        sub_options = browse_page.browse_categories_with_xpath(browse_page.sub_cat_dress_list)
        assert (all(item in sub_options for item in ("CASUAL DRESSES","EVENING DRESSES","SUMMER DRESSES")))
        browse_page.click(browse_page.t_shirts)
        assert browse_page.is_visible(browse_page.tshirts_page) is True
