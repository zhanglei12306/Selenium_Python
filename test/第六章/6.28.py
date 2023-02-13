# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
js = "document.getElementById('kw').value = ‘selenium'"
driver.execute_script(js)
driver.quit()

