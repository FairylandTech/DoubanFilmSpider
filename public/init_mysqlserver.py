# coding: utf8
""" 
@File: init_mysqlserver.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 18:22
"""

import pymysql
import config


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
            connect = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database='mysql',
            )
            try:
                sql_create_database = f"create database if not exists {self.database} charset utf8mb4;"
                cursor = connect.cursor()
                cursor.execute(query=sql_create_database)
                cursor.close()
                connect.commit()
                connect.close()
                try:
                    connect = pymysql.connect(
                        host=self.host,
                        port=self.port,
                        user=self.user,
                        password=self.password,
                        database=self.database,
                    )
                    return connect
                except Exception as error:
                    return error
            except Exception as error:
                return error
        except Exception as error:
            return error


