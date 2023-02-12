#coding=utf-8
from selenium import webdriver
#加载chrome webdriver驱动
driver = webdriver.Chrome()
#打开百度首页
driver.get('https://www.baidu.com') 
#在搜索输入框中输入字符
driver.find_element_by_class_name('s_ipt').send_keys('python') 
