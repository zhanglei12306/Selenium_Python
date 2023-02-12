#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
#加载chrome webdriver驱动
driver = webdriver.Chrome()
#打开百度首页
driver.get('https://www.baidu.com')
#在百度首页点击 新闻 超链接"
driver.find_element(By.LINK_TEXT, '新闻').click()


