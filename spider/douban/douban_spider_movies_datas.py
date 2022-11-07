# coding: utf8
""" 
@File: douban_spider_movies_datas.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/8 0:39
"""

from spider.public.init_mysqlserver import ConnectMySQL

class FindDoubanSpiderMoviesSimplesDatas(ConnectMySQL):
    
    def movies_details_save(self):
        connect = self.mysql()
        cursor = connect.cursor()
        try:
            sql_msg = "select tb_douban_movies.tb_movies_simple_info.url " \
                      "from tb_douban_movies.tb_movies_simple_info ;"
            cursor.execute(query=sql_msg)
            movies_url = cursor.fetchall()
            for url in movies_url:
                movie_url = url[0]
        except Exception as error:
            print(error)
            exit(1)
        cursor.close()
        connect.close()



