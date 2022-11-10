# coding: utf8
"""
@File: apply.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 15:13
"""

from spider.douban.douban_get_movies_url import SpiderDoubanMoviesInit
from spider.douban.douban_movies_simples_datas_cleaning import SpiderDoubanMoviesSimplesDatasCleaning
from spider.douban.douban_get_movies_details import SpiderDoubanMoviesDetails


def spider_run():
    # 1. 获取数据
    SpiderDoubanMoviesInit().batch_save_movies_url()
    # 2. 逻辑删除重复数据
    # print('处理重复URL...')
    SpiderDoubanMoviesSimplesDatasCleaning().movies_url_datas_unique()
    # 3. 获取详细数据
    SpiderDoubanMoviesDetails().batch_save_movies_details()
    print('Done!')


