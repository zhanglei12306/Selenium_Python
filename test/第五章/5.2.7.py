#coding=utf-8
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://passport.meituan.com/account/unitivelogin?")
driver.find_element(By.XPATH, '//*[@id="login-email"]').send_keys('python')

