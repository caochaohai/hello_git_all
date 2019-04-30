import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddContactPage(BaseAction):

    add_name = By.XPATH, "//*[@text='姓名']"
    add_tel = By.XPATH, "//*[@text='电话']"

    @allure.step(title="添加联系人--输入姓名")
    def input_add_name(self, content):
        allure.attach("输入姓名---", content)
        self.input(self.add_name, content)


    @allure.step(title="添加联系人--输入电话")
    def input_add_tel(self, content):
        allure.attach("输入姓名---", content)
        self.input(self.add_tel, content)