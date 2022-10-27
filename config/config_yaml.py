# coding: utf8
""" 
@File: config_yaml.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 18:25
"""

from typing import Union, Any
import yaml
import config


class ConfigYaml(object):
    """读取配置文件"""

    def __init__(self, yaml_file: Any):
        self.yaml_file = yaml_file

    def get_config(self, keyword: str) -> Union[dict, Exception]:
        """
        获取配置文件
        :param keyword: yaml配置的一级key 
        :return: 一级key对象的values
        """
        with open(file=self.yaml_file, mode='r', encoding='utf-8') as yaml_file:
            yaml_config: dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
            try:
                return yaml_config.get(f'{keyword}')
            except Exception as error:
                return error
        

