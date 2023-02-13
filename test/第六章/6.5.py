#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# 获取句柄
print(driver.current_window_handle)