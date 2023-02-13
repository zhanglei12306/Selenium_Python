#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
#执行后，控制台打印“新闻”
print(driver.find_element_by_link_text("新闻").text)
