#coding=utf-8
from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("https://passport.meituan.com/account/unitivelogin?")
driver.find_element_by_xpath('//*[@id="login-email"]').send_keys('134')
