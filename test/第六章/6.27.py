#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
#����ActionChains��
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
bg_config = driver.find_element_by_link_text("����")
ActionChains(driver).move_to_element(bg_config).perform()
driver.find_element_by_link_text("��������").click()
time.sleep(3)
se = driver.find_element_by_id("nr")
Select(se).select_by_visible_text("ÿҳ��ʾ20��")
ops = Select(se).first_selected_option
print(ops.text)
driver.quit()
