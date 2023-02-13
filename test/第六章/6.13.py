#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
#刷新当前页面
driver.refresh()