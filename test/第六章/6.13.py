#coding=utf-8
from selenium import webdriver  
driver = webdriver.Chrome()
driver.get('https://www.baidu.com') #打开百度主页面
#执行后，控制台打印“百度一下”
print(driver.find_element_by_id('su').get_attribute('value'))