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
# 获取全部配置信息
__SETTINGS = ConfigYaml(yaml_file=os.path.join(BASE_DIR, 'config.yaml'))
# 爬虫配置
__SPIDER_CONFIG: dict = __SETTINGS.get_config(keyword='spider')
# 数据库连接信息配置
__MYSQL_CONFIG: dict = __SPIDER_CONFIG.get('mysql')
MYSQL_HOST = __MYSQL_CONFIG.get('host')
MYSQL_PORT = __MYSQL_CONFIG.get('port')
MYSQL_USER = __MYSQL_CONFIG.get('user')
MYSQL_PASSWORD = __MYSQL_CONFIG.get('password')
MYSQL_DATABASE = __MYSQL_CONFIG.get('database')





