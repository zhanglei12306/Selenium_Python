#coding=utf-8
# 引用 'webdriver' 模块
from selenium import webdriver
#启动谷歌浏览器
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
#执行后，输入框输入字符“Selenium”
driver.find_element_by_id('kw').send_keys("Selenium")

