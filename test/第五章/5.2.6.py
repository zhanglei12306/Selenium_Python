#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element(By.CSS_SELECTOR, '.s_ipt').send_keys('python')

