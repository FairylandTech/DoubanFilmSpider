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
        
    def mysql(self):
        """
        创建mysql连接
        :return: 数据库连接对象
        """
        try:
            connnect = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            
            return connnect
        except Exception as error:
            return error


