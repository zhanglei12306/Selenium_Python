#coding=utf-8
from selenium import webdriver
#导入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
bg_config = driver.find_element_by_link_text("设置")
#这里使用方法move_to_element模拟将鼠标悬停在超链接"设置"
ActionChains(driver).move_to_element(bg_config).perform()
#鼠标悬停时，定位元素，超链接"搜索设置"；然后实现单击操作。
driver.find_element_by_link_text("搜索设置").click()
driver.quit()