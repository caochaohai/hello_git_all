import pytest


from base.base_analysis import data_analysis
from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()

        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", data_analysis("address_add_data","test_address_add"))
    def test_address_add(self, args):
        name = args["name"]
        tel = args["tel"]
        self.page.address_list_page.click_add_message_button()
        self.page.add_contact_page.input_add_name(name)
        self.page.add_contact_page.input_add_tel(tel)
        self.page.add_contact_page.press_back()
