#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xjl
# datetime:2019/12/30 19:39
# software: PyCharm
"""自己手动实现一个下载目标url文档的代码
    1 找到目标的网址
    2 在本地新建文件夹
    3 保存到文件夹中
   
"""
import requests
import urllib
from urllib.request import urlretrieve
import re
import os
from bs4 import BeautifulSoup


#输出地址
outputdir = os.getcwd()+"/tdir/"
if not os.path.exists(outputdir.strip().rstrip("\\")):
    os.makedirs(outputdir)
#目标url
turl = "https://www.kancloud.cn/zlt2000/microservices-platform/919412";

 # 设置请求头，字典格式 cookie登陆后可换
form_header = {"cookie": "mycookie"}
#拼接用
clear_url = "https://www.kancloud.cn/zlt2000/microservices-platform/";

file_content={}
link_list=[]
  # 保存url指定内容
def file_down(url,file_name,short_href):
     
    html = requests.get(url, headers=form_header).text  # 获取网页内容

    file_content[file_name]=str(html)
    link_list.append(short_href)
   
 
# 下载list内容
def get_list(URL):
    html = requests.get(URL).text  # 获取网页内容   

    
    
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf8')
    # # ^abc.*?qwe$
    li_list = soup.find('div',class_='catalog').find_all('li')
    # # pic_url = re.findall('"https://cdn.pixabay.com/photo/""(.*?)",',html,re.S)
    
    for tab in li_list:
        short_href = tab.find('a').attrs['href']
        name = tab.find('a').text
        name=name.replace('/','-')
        file_down(clear_url+short_href,outputdir+short_href+".html",short_href)
        print(name)


 
 
# 下载目标 到本地
def downlocal():
    for k in file_content:
        with open(k, 'w',encoding='utf8') as f:
            f.write(file_content[k])
            f.close()
    # urlretrieve(IMAGE_URL, './image2.png')
 
 
# 处理list中的url
def handle_list():
    for k in file_content:
        cus=file_content[k]
        for num in link_list:
            # cus=cus.replace('href="'+num,'href="'+num+".html")
            cus=cus.replace('"path":"'+num,'"path":"'+num+".html")
        file_content[k]=cus
 
# # 下载目标网站的资源
# def zip_down(url):
#     filename = "./tomcat.zip"
#     try:
#         urlretrieve(url, filename)
#     except urllib.ContentTooShortError:
#         print('Network conditions is not good.Reloading.')
#         zip_down(url, filename)
 
 
if __name__ == '__main__':
   
    get_list(turl)
    handle_list()
    downlocal()

    # file_down(turl,outputdir+"919412"+".html")
