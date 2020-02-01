#FireFlieStudio
import random

global proxies
proxies=[]
def pipe():
    global proxies
    if len(proxies) < 1:
        proxy_url='http://www.xiladaili.com/http/' + str(random.randrange(2001))
        proxies=spyder(proxy_url).xpath("//tr/td[1]/text()")
    proxy={'http': proxies.pop()}
    return proxy



import requests
from lxml import etree
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def spyder(url,pro='off',down='off'):
    while True:
        try:
            if pro == 'off' :
                resp=requests.get(url=url,timeout=10, verify=False)
            elif pro == 'on' :
                proxy=pipe()
                resp=requests.get(url=url,proxies=proxy,timeout=10, verify=False)
                print('使用代理成功' + str(proxy))
            if resp.status_code != 200 :
                print('[错误的返还码:' + resp.status_code + '!]')
                continue
            if len(resp.text) < 2 :
                print('[返还数据为空!]')
                continue
        except:
            print('[请求超时!]' + str(proxy))
            continue
        else:
            source_encoding = resp.apparent_encoding or resp.encoding
            if down == 'off' :
                return etree.HTML(resp.content.decode(source_encoding, errors="ignore"))
            elif down == 'on' :
                return resp.content


import os
def down(url,name='null',mod='txt',pro='off'):
    datas=spyder(url,pro=pro,down='on')
    if name == 'null' :
        name=os.path.basename(url)
    if mod == 'txt' :
        write_txt(name,datas)
    elif mod == 'picv' :
        write_picv(name,datas)


import os
def write_txt(name,datas):
    with open(name,'wb') as f:
        f.write((datas).decode().encode())
        f.close()
        

import os
def write_picv(name,datas):
    with open(name,'wb') as f:
        f.write(datas)
        f.close()
        
        
import os
def write(name,datas):
    with open(name,'w') as f:
        f.write(datas)
        f.close()

import os
def mkdir(name):
    if not os.path.isdir(name):
        os.mkdir(name)


import os 
def cd(name):
    if os.path.isdir(name):
        os.chdir(name)


