# coding: utf8
""" 
@File: douban_movies_simples_datas_cleaning.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/8 0:39
"""

from spider.public.init_mysqlserver import ConnectMySQL

class SpiderDoubanMoviesSimplesDatasCleaning(ConnectMySQL):
    
    def movies_url_datas_unique(self):
        connect = self.mysql()
        cursor = connect.cursor()
        try:
            sql_msg = "select count(tb_douban_movies.tb_movies_simple_info.url), tb_douban_movies.tb_movies_simple_info.url " \
                      "from tb_douban_movies.tb_movies_simple_info " \
                      "where is_delete = false " \
                      "group by tb_douban_movies.tb_movies_simple_info.url " \
                      "order by count(tb_douban_movies.tb_movies_simple_info.url) desc ;"
            cursor.execute(query=sql_msg)
            movies_url = cursor.fetchall()
            for index, url in movies_url:
                index: int
                url: str
                if index > 1:
                    num = index - 1
                    sql_msg = f"update tb_douban_movies.tb_movies_simple_info " \
                              f"set tb_douban_movies.tb_movies_simple_info.is_delete = True " \
                              f"where url = '{url}' " \
                              f"order by id desc " \
                              f"limit {num} ;"
                    try:
                        cursor.execute(query=sql_msg)
                    except Exception as error:
                        print(error)
                        exit(1)
        except Exception as error:
            print(error)
            exit(1)
        print('逻辑删除重复数据成功')
        cursor.close()
        connect.commit()
        connect.close()



