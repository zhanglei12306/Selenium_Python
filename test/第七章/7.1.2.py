from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://passport.ctrip.com/user/reg/home")
driver.find_element(By.CSS_SELECTOR,"#agr_pop > div.pop_footer > a.reg_btn.reg_agree").click()
time.sleep(3)
#以下是为了获取滑块元素
sour=driver.find_element(By.CSS_SELECTOR,"#slideCode > div.cpt-drop-box > div.cpt-drop-btn")
print( sour.size['width'])
print(sour.size["height"])
#以下是为了获取滑块区域元素
ele=driver.find_element(By.CSS_SELECTOR,"#slideCode > div.cpt-drop-box > div.cpt-bg-bar")
print(ele.size['width'])
print(ele.size["height"])