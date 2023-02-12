#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#打开百度首页
driver.get('https://www.baidu.com')
#在搜索输入框中输入文本
driver.find_element(By.ID, 'kw').send_keys('python')


