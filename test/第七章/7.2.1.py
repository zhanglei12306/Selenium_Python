from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://user.qunar.com/passport/login.jsp?")
driver.maximize_window()
time.sleep(4)
#对页面截图
driver.save_screenshot("qu.png")
