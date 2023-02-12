#coding=utf-8
#打开百度首页
driver.get('https://www.baidu.com') 
#打开新闻
driver.find_element_by_partial_link_text('新').click()
