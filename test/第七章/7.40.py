#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
#以下请输入html文件的完整路径。
driver.get("xxx/beijing.html")
res = driver.find_elements_by_xpath("//*[starts-with(@id,'beijing')]")

for r in res:
    print(r)
    print(type(r))
