"""
Author:goblinM
Date:2020-01-15
Describe:登录类层
"""
from selenium.webdriver.common.by import By

from test_page_object.object_layer.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, open_url):
        super().__init__(driver, open_url)
        self.login_page_loc = (By.CLASS_NAME, "login-btn")  # ("class name", "login-btn")
        self.email_loc = (By.ID, "email")  # ("id", "email")
        self.password_loc = (By.ID, "password")  # ("id", "password")
        self.login_btn_loc = (By.CLASS_NAME, "login-btn")  # ("class name", "login-btn")

    def open_home_page(self):
        """打开首页"""
        self.open()

    def email_operate(self, email):
        """输入账号"""
        self.find_element(*self.email_loc).send_keys(email)

    def password_operate(self, password):
        """输入密码"""
        self.find_element(*self.password_loc).send_keys(password)

    def open_login_page(self):
        """打开登录页"""
        self.find_element(*self.login_page_loc).click()

    def login_btn_operate(self):
        """点击登录"""
        self.find_element(*self.login_btn_loc).click()

