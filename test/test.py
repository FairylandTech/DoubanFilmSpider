# coding: utf8
"""
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 15:13
"""

import config
from spider.public.build_headers import BuildHeaders
from spider.save.connect_mysql import ConnectMySQL


if __name__ == '__main__':
    # print(BuildHeaders.headers())
    # print(config.MYSQL_HOST)
    print(ConnectMySQL.mysql())
    pass
