#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
jq = "$('#kw').val('selenium')"
driver.execute_script(jq)
#以下代码实现单击"百度以下"按钮
jq = "$('#su').click()"
driver.execute_script(jq)
driver.quit()
