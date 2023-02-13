#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
#控制台打印tile“百度一下，你就知道”
print(driver.title)
