#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
#导入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
bg_config = driver.find_element_by_link_text("设置")
#模拟将鼠标悬浮于超链接“设置”
ActionChains(driver).move_to_element(bg_config).perform()
#鼠标悬停时，定位元素，超链接"搜索设置"；然后实现单击操作。
driver.find_element_by_link_text("搜索设置").click()
time.sleep(3)
se = driver.find_element_by_id("nr")
#index索引是从0开始的，选择1则表示第二个选项。
Select(se).select_by_index(1)
driver.quit()
