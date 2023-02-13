#coding=utf-8
from selenium import webdriver  # import 'webdriver' 模块
import time
#加载chrome webdriver驱动
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
#打开百度主页面
driver.get('https://www.cnblogs.com') 
print("before login:")
#打印全部cookie
for cookie_detail in driver.get_cookies():
    print(cookie_detail)
#等待30秒，方便手动干预输入账号、密码
time.sleep(30) 
print("after login:")
for cookie_detail in driver.get_cookies():
    print(cookie_detail)
driver.quit()
