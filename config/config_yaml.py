# coding: utf8
""" 
@File: config_yaml.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 18:25
"""
from typing import Union

import yaml


class ConfigYaml(object):
    
    def __init__(self, yaml_file: str):
        self.yaml_file = yaml_file
        
    @classmethod
    def get_config(cls, keyword: str) -> Union[dict, Exception]:
        with open(file=cls().yaml_file, mode='r', encoding='utf-8') as yaml_file:
            yaml_config: dict = yaml.load(cls().yaml_file, Loader=yaml.FullLoader)
            try:
                return yaml_config.get(f'{keyword}')
            except Exception as error:
                return error
        

