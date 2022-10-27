# coding: utf8
""" 
@File: connect_mysql.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 18:22
"""

import pymysql
import config
from typing import Any


class ConnectMySQL(object):
    """连接数据库"""
    
    def __init__(self):
        self.host = config.MYSQL_HOST
        self.port = config.MYSQL_PORT
        self.user = config.MYSQL_USER
        self.password = config.MYSQL_PASSWORD
        self.database = config.MYSQL_DATABASE
        
    @classmethod
    def mysql(cls) -> Any:
        try:
            connnect = pymysql.connect(
                host=cls().host,
                port=cls().port,
                user=cls().user,
                password=cls().password,
                database=cls().database,
                charset='utf-8'
            )
            
            return connnect.cursor()
        except Exception as error:
            return error
