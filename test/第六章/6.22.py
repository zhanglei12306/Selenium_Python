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
#ģ�⽫��������ڳ����ӡ����á� 
ActionChains(driver).move_to_element(bg_config).perform()
#�����ͣʱ����λԪ�أ�������"��������"��Ȼ��ʵ�ֵ���������
driver.find_element_by_link_text("��������").click()
time.sleep(3)
se = driver.find_element_by_id("nr")
#index�����Ǵ�0��ʼ�ģ�ѡ��1���ʾ�ڶ���ѡ�
Select(se).select_by_index(1)
driver.quit()
