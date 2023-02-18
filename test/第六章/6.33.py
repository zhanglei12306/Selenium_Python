#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
#打开主页面QQ邮箱登录页面
driver.get('https://en.mail.qq.com/cgi-bin/loginpage')
#驱动切换到iframe
driver.switch_to.frame("login_frame")
#驱动切换到iframe外
# driver.switch_to.default_content("login_frame")
#对用户名赋值
driver.find_element_by_id('u').send_keys('test')
#退出浏览器操作
driver.quit()
#打印"测试完成"标记。
print('test complete!')