###
###������Ƶ�ѳ��棬ѧϰ��������ϵ����qq:2574674466###
###
#coding=utf-8
from selenium import webdriver 
driver = webdriver.Chrome()
#����ҳ��QQ�����¼ҳ��
driver.get('https://en.mail.qq.com/cgi-bin/loginpage') 
#�����л���iframe 
driver.switch_to.frame("login_frame")
#���û�����ֵ
driver.find_element_by_id('u').send_keys('test')
#�˳����������
driver.quit()
#��ӡ"�������"��ǡ�
print('test complete!')
