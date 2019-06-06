# -*- encoding=utf8 -*-
__author__ = "jason"

from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest.utils.selenium_proxy import WebChrome


driver = WebChrome()
driver.implicitly_wait(20)
# -*- encoding=utf8 -*-
__author__ = "User"

from airtest.core.api import *

auto_setup(__file__)

driver.get("http://cqb-gz.test.sh-weiyi.com/cqb-base-mgr-fe/app.html#/login")
driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/button/span").click()
    #关闭
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("admin")
    #输入账号
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("shwy-1212")
    #输入密码
driver.find_element_by_xpath("//input[@placeholder='验证码']").send_keys("shwy")
    #输入密码
    #点击确认
driver.find_element_by_xpath("//button[@style='width: 100%;']").click()
sleep(10)