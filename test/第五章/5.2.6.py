#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_css_selector('.s_ipt').send_keys('python')
