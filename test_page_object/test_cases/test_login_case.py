"""
Author:goblinM(mmx)
Date:2020-01-15
Describe:业务层(测试用例层)
"""
from selenium import webdriver
import ddt
from test_page_object.data_layer.analysis_data import YamlMethods
from test_page_object.logic_layer.user_login_logic import user_login
import unittest


def test_user_login():
    """测试登录界面"""
    driver = webdriver.Chrome()
    open_url = "https://www.polyv.net/"
    user_email = "mominxin@polyv.net"
    user_password = "mmx123456"
    user_login(driver, open_url, user_email, user_password)


# @ddt.ddt
class TestLoginCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = YamlMethods().single_yaml_load()

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        pass

    def set_login_information(self, key):
        """设置信息"""
        data = self.data.get(key)
        email = data.get("email")
        password = data.get("password")
        open_url = data.get("open_url")
        return email, password, open_url

    # @ddt.file_data("test_right_login.yaml")
    def test_right_login(self):
        """正确信息登录"""
        user_email, user_password, open_url = self.set_login_information("right_login")
        user_login(self.driver, open_url, user_email, user_password)

    # @unittest.skip
    def test_wrong_login(self):
        """错误信息登录"""
        user_email, user_password, open_url = self.set_login_information("wrong_login")
        user_login(self.driver, open_url, user_email, user_password)


if __name__ == '__main__':
    # unittest.main()
    # 单个用例执行
    suits = unittest.TestSuite()
    suits.addTest(TestLoginCase("test_right_login"))
    suits.addTest(TestLoginCase("test_wrong_login"))
    runner = unittest.TextTestRunner()
    runner.run(suits)
