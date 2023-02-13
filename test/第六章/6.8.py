#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#打开百度首页
driver.get('https://www.baidu.com')
#判断元素是否被可用
driver.find_element(By.ID, 'kw').is_enabled()