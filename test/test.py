# coding: utf8
"""
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 15:13
"""

from spider.public.init_mysqlserver import ConnectMySQL
import re
from spider.douban.douban_get_movies_url import SpiderDoubanMoviesInit
from spider.douban.douban_movies_simples_datas_cleaning import SpiderDoubanMoviesSimplesDatasCleaning
from spider.douban.douban_get_movies_details import SpiderDoubanMoviesDetails


if __name__ == '__main__':
    # 获取数据
    SpiderDoubanMoviesInit().batch_save_movies_url()
    # 逻辑删除重复数据
    # SpiderDoubanMoviesSimplesDatasCleaning().movies_url_datas_unique()
    # 获取详细数据
    # SpiderDoubanMoviesDetails().batch_save_movies_details()
    pass
