# coding: utf8
""" 
@File: test02.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/8 0:45
"""

from spider.douban.douban_get_movies_details import SpiderDoubanMoviesDetails

if __name__ == '__main__':
    SpiderDoubanMoviesDetails().batch_save_movies_details()

