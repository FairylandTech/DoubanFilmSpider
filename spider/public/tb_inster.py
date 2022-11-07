# coding: utf8
""" 
@File: tb_inster.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/28 14:07
"""

from spider.public.mysqlserver_execute_command import ExecuteSQL
from spider.public.tb_builtin_select import BuiltinSelect


class InsterTables(ExecuteSQL):
    """数据插入"""
    
    def __init__(self):
        super(InsterTables, self).__init__()
        
    def insert_tb_director_info(self, name: str, sex: str, introduction: str, link: str):
        """
        导演表数据写入
        :param name: 导演姓名 
        :param sex: 导演性别
        :param introduction: 导演介绍 
        :param link: 导演链接
        :return: 
        """
        if sex == '男' or sex == '女':
            if sex == '男':
                sex = 0
            else:
                sex = 1
            sql_msg = "insert into tb_director_info (name, sex, introduction, link) " \
                      f"values ('{name}', {sex}, '{introduction}', '{link}') ;"
            self.exec_sql(sql_msg=sql_msg)
        else:
            return 1
    
    def insert_tb_player_info(self, name: str, sex: str, introduction: str, link: str):
        """
        演员表数据插入
        :param name: 演员姓名 
        :param sex: 演员性别
        :param introduction: 演员介绍
        :param link: 演员链接
        :return:
        """
        if sex == '男' or sex == '女':
            if sex == '男':
                sex = 0
            else:
                sex = 1
            sql_msg = "insert into tb_player_info (name, sex, introduction, link) " \
                      f"values ('{name}', {sex}, '{introduction}', '{link}') ;"
            self.exec_sql(sql_msg=sql_msg)
        else:
            return 1
        
    def insert_tb_movies_info(self,
                              name: str,
                              director: str,
                              assistant_director: str,
                              screenwriter: str,
                              player_master: str,
                              player: str,
                              first_play: str,
                              type: str,
                              country: str,
                              length: int,
                              introduction: str,
                              link: str):
        """
        电影表数据插入
        :param name: 电影名称
        :param director: 导演id
        :param assistant_director: 副导演; 多个副导演使用,分隔
        :param screenwriter: 电影编剧; 多个编剧使用,分隔
        :param player_master: 电影主演
        :param player: 电影演员; 多个演员使用,分隔
        :param first_play: 电影首映时间
        :param type: 电影类型; 多个类型使用,分隔
        :param country: 制片国家; 多个国家使用,分隔
        :param length: 电影时长
        :param introduction: 电影介绍
        :param link: 电影url
        :return: 
        """
        # 获取导演id
        director_id = BuiltinSelect().select_tb_director_info_id(name=director)
        # 获取主演id
        player_master_id = BuiltinSelect().select_tb_player_info_id(name=player_master)
        sql_msg = "insert into tb_douban_movies.tb_movies_info (" \
                  "name, " \
                  "director_id, " \
                  "assistant_director, " \
                  "screenwriter, " \
                  "player_master_id, " \
                  "player, " \
                  "first_play, " \
                  "type, " \
                  "country, " \
                  "length, " \
                  "introduction, " \
                  "link) " \
                  "values (" \
                  f"'{name}', " \
                  f"{director_id}, " \
                  f"'{assistant_director}', " \
                  f"'{screenwriter}', " \
                  f"{player_master_id}, " \
                  f"'{player}', " \
                  f"'{first_play}', " \
                  f"'{type}', " \
                  f"'{country}', " \
                  f"{length}, " \
                  f"'{introduction}', " \
                  f"'{link}') ;"
        self.exec_sql(sql_msg=sql_msg)
        
    def insert_tb_movies_simple_info(self, title: str, url: str):
        sql_msg = f"insert into tb_douban_movies.tb_movies_simple_info (" \
                  f"title, " \
                  f"url) " \
                  f"values (" \
                  f"'{title}', " \
                  f"'{url}'" \
                  f") ;"
        self.exec_sql(sql_msg=sql_msg)
        
        
if __name__ == '__main__':
    # InsterTables().insert_tb_director_info(name='张三', sex='男', introduction='我是张三11', link='https://baidu.com')
    # InsterTables().insert_tb_player_info(name='张小三', sex='男', introduction='我是张小三', link='https://google.com')
    # InsterTables().insert_tb_movies_info(
    #     name='自拍',
    #     director='张三',
    #     assistant_director='李四,王五',
    #     screenwriter='李四四,王五五',  # 赵六六,老八八
    #     player_master='张小三',
    #     player='赵六,老八',
    #     first_play='2022-09-30',
    #     type='剧情,素人',
    #     country='日本,新加坡',
    #     length=137,
    #     introduction='自拍',
    #     link='https://baidu.com'
    # )
    pass


