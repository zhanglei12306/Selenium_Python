###
###配套视频已出版，学习有疑问联系作者qq:2574674466###
###
#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
#浏览器向后
driver.back();
#浏览器向前
driver.forward();
