import time

import pytest

from ecommerce.page_objects.browse_categories import BrowseCategories
from ecommerce.page_objects.testdata import TestData


@pytest.mark.usefixtures("chrome_driver_init")
class TestSearchBox:
    """Search the store
    """
    def test_search_box(self):
        """search in search box"""
        browse_page = BrowseCategories(self.driver)
        browse_page.enter_text(browse_page.search_box, "dresses")
        options = browse_page.browse_categories_with_css(browse_page.search_results_list)
        assert (all(item in options for item in TestData.search_list_results))
        browse_page.click(browse_page.butn_search)
        assert browse_page.is_visible(browse_page.product_listing)
