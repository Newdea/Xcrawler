#!/usr/bin/env python3          # 标准注释
# -*- coding:utf-8 -*-          # 表示.py文件本身使用标准UTF-8编码

"""get dynamic webpage content. run good ~"""  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Newdea'  # 变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

# url of list 1
url = 'http://music.163.com/#/discover/playlist'

# 用PhontomJS创建一个Selenium 的webdriver
wdriver = webdriver.PhantomJS()

# 准备好存储歌单的csv文件 gbk
csv_file = open('song_list.csv','w',encoding='gb18030',newline='',)
writer = csv.writer(csv_file)
writer.writerow(['标题', '播放数', '链接'])


# 解析每页，直到下一页为空
while url != "javascript:void(0)":
    # 用webdriver 加载页面
    wdriver.get(url)
    #切换到内容的Frame
    wdriver.switch_to.frame('contentFrame')
    # 定位歌单标签find all -- #m-pl-container
    data = wdriver.find_element_by_id('m-disc-pl-c').\
        find_elements_by_tag_name('li')
    # 解析该页内所有歌单
    
    for i in range(len(data)):
        #获取播放数 find_element_by_tag_name('span').\
        numBroaadcast = data[i].find_element_by_class_name('nb').text
        # 如果播放数大于500万，
        if '万' in numBroaadcast and int(numBroaadcast.split('万')[0]) > 500:
            # 获取其封面
            msk = data[i].find_element_by_css_selector('a.msk')
            # 写入文件中
            writer.writerow([msk.get_attribute('title'),numBroaadcast,msk.get_attribute('href')])
    # 定位下一页的url
    url = wdriver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')
csv_file.close()


