"""
Author:goblinM
Date:2020-01-15
Describe:用户登录的逻辑处理页面
"""
from object_layer.login_page import LoginPage


def user_login(driver, open_url, email, password):
    """检验账号密码是否能登录"""
    login_page = LoginPage(driver,open_url)
    login_page.open_home_page()
    login_page.open_login_page()
    login_page.email_operate(email)
    login_page.password_operate(password)
    login_page.login_btn_operate()

