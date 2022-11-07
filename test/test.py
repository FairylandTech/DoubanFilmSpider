# coding: utf8
"""
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 15:13
"""

from spider.public.init_mysqlserver import ConnectMySQL
import re
from spider.douban.douban_save_movies_url import BatchedSpiderDoubanMoviesDatas


if __name__ == '__main__':
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='喜剧')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='爱情')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='动作')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='动画')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='悬疑')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='犯罪')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='冒险')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='音乐')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='历史')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='奇幻')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='恐怖')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='战争')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='传记')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='歌舞')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='武侠')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='情色')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='灾难')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='西部')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='纪录片')
    # BatchedSpiderDoubanMoviesDatas().batch_datas(movies_type='短片')
    BatchedSpiderDoubanMoviesDatas().douban_movies_types()
    pass
