#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
bg_config = driver.find_element_by_link_text("����")
ActionChains(driver).move_to_element(bg_config).perform()
#�����ͣʱ����λԪ�أ�������"��������"��Ȼ��ʵ�ֵ���������
driver.find_element_by_link_text("��������").click()
#��ͬҳ����ת��Ҫʱ�䣬���õȴ�ʱ��
time.sleep(3)
se = driver.find_element_by_id("nr")
#��2��textΪ��ÿҳ��ʾ20����
Select(se).select_by_visible_text("ÿҳ��ʾ20��")
driver.quit()
