#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
bg_config = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(bg_config).perform()
#鼠标悬停时，定位元素，超链接"搜索设置"；然后实现单击操作。
driver.find_element_by_link_text("搜索设置").click()
#不同页面跳转需要时间，设置等待时间
time.sleep(3)
se = driver.find_element_by_id("nr")
#第2项text为“每页显示20条”
Select(se).select_by_visible_text("每页显示20条")
driver.quit()
