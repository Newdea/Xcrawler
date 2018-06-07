#!/usr/bin/env python3          # 标准注释
# -*- coding:utf-8 -*-          # 表示.py文件本身使用标准UTF-8编码

"""a test hello module"""  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Newdea'  # 变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://wap.baidu.com/')        # open url ,get the content
# send it to bs4_obj
bs4_obj = BeautifulSoup(html.read(),'html.parser')
# find all class='ns-text' 的span 标签
text_list = list(BeautifulSoup.find_all("span", "ns-text"))
for text in text_list:
    print(text.get_text())
html.close()



