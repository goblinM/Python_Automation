# -*- encoding=utf-8 -*-
"""
Author:goblinM
Date: 2020-01-15
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_user_login():
    """
    以Polyv的登录界面举例
    :return:
    """
    # 打开chrome浏览器
    driver = webdriver.Chrome()
    # 页面全屏放大
    driver.maximize_window()
    # 打开官网
    base_url = "https://www.polyv.net/"
    driver.get(base_url)
    # 搜索登录按钮并点击
    login_page = driver.find_element_by_css_selector(".login-btn")
    login_page.click()
    # 登录页面
    sleep(3)
    email = driver.find_element_by_css_selector("#email")
    email.send_keys("xxx")
    password = driver.find_element_by_css_selector("#password")
    password.send_keys("xxx")
    login_btn = driver.find_element_by_css_selector(".login-btn")
    login_btn.click()
    # 关闭网页
    # driver.close()
    # 隐式等待
    # driver.implicitly_wait(30)
    # 显式等待
    # WebDriverWait(driver, 10)


def test_user_login_two():
    # 打开chrome浏览器
    driver = webdriver.Chrome()
    # 页面全屏放大
    driver.maximize_window()
    # 打开官网
    base_url = "https://www.polyv.net/"
    driver.get(base_url)
    driver.find_element(By.CLASS_NAME, "login-btn").click()
    driver.find_element(By.ID, "email").send_keys("xxx")
    driver.find_element(By.ID, "password").send_keys("xxx")
    driver.find_element(By.CLASS_NAME, "login-btn").click()


if __name__ == '__main__':
    # test_user_login()
    test_user_login_two()


