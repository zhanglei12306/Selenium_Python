#coding=utf-8
#打开百度首页
driver.get('https://www.baidu.com') 
#在百度首页点击 新闻 超链接"
driver.find_element_by_link_text('新闻').click() 
