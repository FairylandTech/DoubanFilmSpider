# coding: utf8
""" 
@ File: data_clean.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-04-08
"""
import jieba
import pymysql
import sys
from wordcloud import WordCloud
import re


class ConnectionMySQL:

    def __init__(self):
        self._host = '10.0.12.2'
        self._port = 13306
        self._user = 'root'
        self._password = 'Mysql.pwd_5.8%'
        self._database = 'tb_douban_movies'

    def _connect(self):
        self._conn = pymysql.connect(
            host=self._host,
            port=self._port,
            user=self._user,
            password=self._password,
            database=self._database,
            cursorclass=pymysql.cursors.DictCursor
        )
        self._cur = self._conn.cursor()
        return ...

    def _close(self):
        if self._cur:
            self._cur.close()
        if self._conn:
            self._conn.close()

    def query(self, query):
        try:
            self._connect()
            self._cur.execute(query=query)
            result = self._cur.fetchall()
            return result
        except Exception as error:
            print(error)
        finally:
            self._close()
            
    def update(self, update):
        try:
            self._connect()
            self._cur.execute(query=update)
            self._conn.commit()
        except Exception as error:
            print(error)
        finally:
            self._close()


class KeyWordCloud:

    def __init__(self):
        self.connection_mysql = ConnectionMySQL()
    
    def directors_wordcloud(self):
        query = 'select directors from tb_movies_used_info where is_delete = false limit 10000'
        result = self.connection_mysql.query(query)
        directors_str: str = ''
        for row in result:
            row: dict
            directors_str += row.get('directors')
        text_cut = ''.join(jieba.cut(directors_str))
        wc = WordCloud(font_path='../static/ttf/方正粗黑宋简体.ttf', width=1024, height=768, background_color='white').generate(text_cut)
        wc.to_file('directors_wordcloud.png')
        
    def actors_wordcloud(self):
        query = 'select actors from tb_movies_used_info where is_delete = false limit 10000'
        result = self.connection_mysql.query(query)
        actors_str: str = ''
        for row in result:
            row: dict
            actors_str += row.get('actors')
        text_cut = ''.join(jieba.cut(actors_str))
        wc = WordCloud(font_path='../static/ttf/方正粗黑宋简体.ttf', width=1024, height=768, background_color='white').generate(text_cut)
        wc.to_file('actors_wordcloud.png')
        
    def summary_wordcloud(self):
        query = 'select summary from tb_movies_used_info where is_delete = false limit 10000'
        result = self.connection_mysql.query(query)
        summary_str: str = ''
        for row in result:
            row: dict
            summary_str += row.get('summary')
        text_cut = ''.join(jieba.cut(summary_str))
        wc = WordCloud(font_path='../static/ttf/方正粗黑宋简体.ttf', width=1024, height=768, background_color='white').generate(text_cut)
        wc.to_file('summary_wordcloud.png')
        
    def title_wordcloud(self):
        query = 'select title from tb_movies_used_info where is_delete = false limit 10000'
        result = self.connection_mysql.query(query)
        title_str: str = ''
        for row in result:
            row: dict
            title_str += row.get('title')
        text_cut = ''.join(jieba.cut(title_str))
        wc = WordCloud(font_path='../static/ttf/方正粗黑宋简体.ttf', width=1024, height=768, background_color='white').generate(text_cut)
        wc.to_file('title_wordcloud.png')
        
    def movie_type_wordcloud(self):
        query = 'select movie_type from tb_movies_used_info where is_delete = false limit 10000'
        result = self.connection_mysql.query(query)
        movie_type_str: str = ''
        for row in result:
            row: dict
            movie_type_str += row.get('movie_type')
        text_cut = ''.join(jieba.cut(movie_type_str))
        wc = WordCloud(font_path='../static/ttf/方正粗黑宋简体.ttf', width=1024, height=768, background_color='white').generate(text_cut)
        wc.to_file('movie_type_wordcloud.png')
        
        
class MainProgram:
    
    def __init__(self):
        self.connection_mysql = ConnectionMySQL()
        self.key_wordcloud = KeyWordCloud()
        
    def movies_long_clean(self):
        query = 'select id, movie_long from tb_movies_used_info where is_delete = false ;'
        result = self.connection_mysql.query(query=query)
        for row in result:
            row: dict
            _id = row.get('id')
            movies_long = row.get('movie_long')
            if not re.match(r'\d', movies_long):
                update = 'update tb_movies_used_info set is_delete = true where id = {}'.format(_id)
                self.connection_mysql.update(update=update)


if __name__ == '__main__':
    def test():
        connection_mysql = ConnectionMySQL()
        query = 'select id, movie_long from tb_movies_used_info where is_delete = false ;'
        result = connection_mysql.query(query=query)
        for row in result:
            row: dict
            _id = row.get('id')
            movies_long = row.get('movie_long')
            if not re.match(r'\d', movies_long):
                update = 'update tb_movies_used_info set is_delete = true where id = {}'.format(_id)
                connection_mysql.update(update=update)


    test()

    # 词云图    
    # kw = KeyWordCloud()
    # kw.directors_wordcloud()
    # kw.actors_wordcloud()
    # kw.summary_wordcloud()
    # kw.title_wordcloud()
    # kw.movie_type_wordcloud()
    
    print('done...')
