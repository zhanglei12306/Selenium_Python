#coding=utf-8
from selenium import webdriver
#����ActionChains��
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
bg_config = driver.find_element_by_link_text("����")
#����ʹ�÷���move_to_elementģ�⽫�����ͣ�ڳ�����"����"
ActionChains(driver).move_to_element(bg_config).perform()
#�����ͣʱ����λԪ�أ�������"��������"��Ȼ��ʵ�ֵ���������
driver.find_element_by_link_text("��������").click()
driver.quit()
