from selenium import webdriver
import  time
from PIL import Image
driver = webdriver.Chrome()
driver.get("https://user.qunar.com/passport/login.jsp?")
driver.maximize_window()
time.sleep(4)
driver.save_screenshot("qu.png")
imgcode=driver.find_element_by_id("vcodeImg")
left= imgcode.location['x']
top= imgcode.location['y']
right = left+imgcode.size['width']
bottom = top+imgcode.size['height']
im = Image.open("qu.png")
im = im.crop((left,top,right,bottom))
im.save('t.png')