#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
print(driver.find_element(By.TAG_NAME, 'form').get_attribute('name'))

