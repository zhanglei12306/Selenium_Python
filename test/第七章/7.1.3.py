from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://passport.ctrip.com/user/reg/home")
driver.find_element(By.CSS_SELECTOR,"#agr_pop>div.pop_footer> a.reg_btn.reg_agree").click()
time.sleep(3)
sour=driver.find_element(By.CSS_SELECTOR,"#slideCode>div.cpt-drop-box> div.cpt-drop-btn")
ele=driver.find_element(By.CSS_SELECTOR,"#slideCode>div.cpt-drop-box> div.cpt-bg-bar")
#拖动滑块
ActionChains(driver).drag_and_drop_by_offset(sour,ele.size['width'],-sour.size["height"]).perform()