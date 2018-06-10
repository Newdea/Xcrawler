#!/usr/bin/env python3          # 标准注释
# -*- coding:utf-8 -*-          # 表示.py文件本身使用标准UTF-8编码

""" some lib or framework for scrapy

"""  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Newdea'  # 变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

import re  # regular expression Perl style
import _thread  # 在单线程中执行任何python调用的对象
import queue  # 用队列实现线程间的同步
import configparser  # 读取配置文件的模块
import numpy as np
from urllib import request


def get_random_ua():
    rand_ua = ''
    ua_file = 'ua_file.txt'
    try:
        with open(ua_file) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_proxy = lines[int(idx)]
    except Exception as e:
        print('Exception in random_ua.')
        print(str(e))
    finally:
        return rand_ua


user_agent = get_random_ua()
headers = {
    'user-agent': user_agent,
}
r = request.get('example.com', headers=headers)
