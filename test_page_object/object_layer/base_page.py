"""
Author:goblinM
Date:2020-01-15
Describe:基础类层
"""


class BasePage(object):

    def __init__(self, driver, open_url):
        """初始化driver 以及open_url """
        self.open_url = open_url
        self.driver = driver

    def _open(self):
        """私有方法，打开open_url"""
        self.driver.get(self.open_url)

    def open(self):
        """公有方法"""
        self._open()

    def find_element(self, *loc):
        """
        单个元素定位方法封装
        :param: *loc
        example:
            driver.find_element(By.CLASS_NAME, "login-btn").click()
        """
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        多个元素定位方法封装
        :return:
        """
        return self.driver.find_elements(*loc)

    def max_size_screen(self):
        self.driver.maximize_window()
