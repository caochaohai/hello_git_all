from page.add_contact_page import AddContactPage
from page.address_list_page import AddressListPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def add_contact_page(self):
        return AddContactPage(self.driver)

    @property
    def address_list_page(self):
        return AddressListPage(self.driver)