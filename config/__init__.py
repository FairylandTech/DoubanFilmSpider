# coding: utf8
""" 
@File: __init__.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 18:26
"""

import os
from config.config_yaml import ConfigYaml

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 数据库连接信息配置
MYSQL_CONFIG: dict = ConfigYaml.get_config(keyword='mysql')
MYSQL_HOST = MYSQL_CONFIG.get('host')
MYSQL_PORT = MYSQL_CONFIG.get('port')
MYSQL_USER = MYSQL_CONFIG.get('username')
MYSQL_PASSWORD = MYSQL_CONFIG.get('password')
MYSQL_DATABASE = MYSQL_CONFIG.get('database')




