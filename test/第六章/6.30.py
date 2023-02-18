#coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
element = driver.find_element_by_link_text(u"新闻")
#双击“新闻”
ActionChains(driver).double_click(element).perform()
