#coding=utf-8
from urllib import request
import http.cookiejar
import urllib3
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#����SSL�������Ϣ
urllib6.disable_warnings()
#����CookieJar����
cookie = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
#�ڴ�URL�Ĺ����У��Ὣcookie����Ϣ�����cookie�����С�
req = opener.open('http://sogou.com')
#����cookie����
for i in cookie:
    print(i.name + ":"+ i.value)
