#coding=utf-8
from selenium import webdriver  # import 'webdriver' ģ��
import time
#����chrome webdriver����
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
#�򿪰ٶ���ҳ��
driver.get('https://www.cnblogs.com') 
print("before login:")
#��ӡȫ��cookie
for cookie_detail in driver.get_cookies():
    print(cookie_detail)
#�ȴ�30�룬�����ֶ���Ԥ�����˺š�����
time.sleep(30) 
print("after login:")
for cookie_detail in driver.get_cookies():
    print(cookie_detail)
driver.quit()
