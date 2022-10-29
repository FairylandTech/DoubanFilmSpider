# coding: utf8
""" 
@File: tb_builtin_select.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/30 0:56
"""

from spider.public.mysqlserver_execute_command import ExecuteSQL


class BuiltinSelect(ExecuteSQL):
    """内置查询"""

    def select_tb_director_info_id(self, name: str):
        """
        查询对应导演的id
        :param name: 导演姓名
        :return: 导演id
        """
        _id: int = 0
        sql_msg = "select tb_douban_movies.tb_director_info.id " \
                  "from tb_douban_movies.tb_director_info " \
                  f"where tb_douban_movies.tb_director_info.name = '{name}'"
        try:
            self.cursor.execute(query=sql_msg)
            director_msg = self.cursor.fetchall()
            for director_id in director_msg:
                _id = director_id[0]
            if _id == 0:
                print(f'数据库中没有{name}导演')
                raise Exception(exit(1))
            self.cursor.close()
            self.connect.close()
            return _id
        except Exception as error:
            self.cursor.close()
            self.connect.close()
            print(error)
            exit(1)
            
    def select_tb_player_info_id(self, name):
        """
        查询对应演员的id
        :param name: 演员姓名
        :return: 演员id, 
        """
        _id: int = 0
        sql_msg = "select tb_douban_movies.tb_player_info.id " \
                  "from tb_douban_movies.tb_player_info " \
                  f"where tb_douban_movies.tb_player_info.name = '{name}' ;"
        try:
            self.cursor.execute(query=sql_msg)
            player_msg = self.cursor.fetchall()
            for player_id in player_msg:
                _id = player_id[0]
            if _id == 0:
                print(f'数据中没有{name}演员')
                raise Exception(exit(1))
            self.cursor.close()
            self.connect.close()
            return _id
        except Exception as error:
            self.cursor.close()
            self.connect.close()
            print(error)
            exit(1)
            
            
if __name__ == '__main__':
    # print(BuiltinSelect().select_tb_director_info_id(name='张三'))
    # print(BuiltinSelect().select_tb_player_info_id(name='张小三'))
    # print(BuiltinSelect().select_tb_player_info_id(name='张小三'))
    pass
