#coding=utf-8
#引入Application模块
from pywinauto.application import  Application
import time
app =Application()
#定位到窗口
app = app.connect(title_re="打开",class_name="#32770")
#设置文件路径
app['打开']["EDit1"].SetEditText("D:\soft\ip.txt ")
time.sleep(2)
#单击按钮
app["打开"]["Button1"].click()
print("end")

