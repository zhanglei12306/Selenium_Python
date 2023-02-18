#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("SeleniumTest")
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)