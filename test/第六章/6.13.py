#coding=utf-8
from selenium import webdriver  
driver = webdriver.Chrome()
driver.get('https://www.baidu.com') #�򿪰ٶ���ҳ��
#ִ�к󣬿���̨��ӡ���ٶ�һ�¡�
print(driver.find_element_by_id('su').get_attribute('value'))
