#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
jq = "$('#kw').val('selenium')"
driver.execute_script(jq)
#���´���ʵ�ֵ���"�ٶ�����"��ť
jq = "$('#su').click()"
driver.execute_script(jq)
driver.quit()
