#coding=utf-8
from selenium import webdriver
#����chrome webdriver����
driver = webdriver.Chrome()
#�򿪰ٶ���ҳ
driver.get('https://www.baidu.com') 
#������������������ַ�
driver.find_element_by_class_name('s_ipt').send_keys('python') 
