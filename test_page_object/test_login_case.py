"""
Author:goblinM(mmx)
Date:2020-01-15
Describe:业务层(测试用例层)
"""
from selenium import webdriver

from logic_layer.user_login_logic import user_login


def test_user_login():
    """测试登录界面"""
    driver = webdriver.Chrome()
    open_url = "https://www.polyv.net/"
    user_email = "mominxin@polyv.net"
    user_password = "mmx123456"
    user_login(driver, open_url, user_email, user_password)
