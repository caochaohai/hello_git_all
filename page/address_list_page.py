from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # def __init__(self, driver):
    add_buttton = By.ID, "com.android.contacts:id/floating_action_button"

    def click_add_message_button(self):
        self.click(self.add_buttton)
