# coding: utf8
"""
@File: base.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/18 17:15
"""

from public.mysqlserver_execute_command import ConnectMySQL


def c_score():
    conn = ConnectMySQL().mysql()
    cur = conn.cursor()
    sql_msg_q_1 = "select tb_douban_movies.tb_movies_used_info.id, " \
                  "tb_douban_movies.tb_movies_used_info.score " \
                  "from tb_douban_movies.tb_movies_used_info " \
                  "where tb_douban_movies.tb_movies_used_info.is_delete = false " \
                  "and tb_douban_movies.tb_movies_used_info.score = '0' ;"
    cur.execute(query=sql_msg_q_1)
    query_result = cur.fetchall()
    for row in query_result:
        row: tuple
        did = row[0]
        sql_msg_m_1 = "update tb_douban_movies.tb_movies_used_info " \
                      "set tb_douban_movies.tb_movies_used_info.is_delete = true " \
                      "where tb_douban_movies.tb_movies_used_info.id = {} ;".format(did)
        print(sql_msg_m_1)
        cur.execute(query=sql_msg_m_1)
        conn.commit()
    cur.close()
    conn.close()
    
    
def c_directors():
    conn = ConnectMySQL().mysql()
    cur = conn.cursor()
    sql_msg_q_1 = "select tb_douban_movies.tb_movies_used_info.id, " \
                  "tb_douban_movies.tb_movies_used_info.directors " \
                  "from tb_douban_movies.tb_movies_used_info " \
                  "where tb_douban_movies.tb_movies_used_info.is_delete = false " \
                  "and tb_douban_movies.tb_movies_used_info.directors = '' ;"
    cur.execute(query=sql_msg_q_1)
    query_result = cur.fetchall()
    for row in query_result:
        row: tuple
        did = row[0]
        sql_msg_m_1 = "update tb_douban_movies.tb_movies_used_info " \
                      "set tb_douban_movies.tb_movies_used_info.directors = '无' " \
                      "where tb_douban_movies.tb_movies_used_info.id = {} ;".format(did)
        print(sql_msg_m_1)
        cur.execute(query=sql_msg_m_1)
        conn.commit()
    cur.close()
    conn.close()
    
    
def c_actors():
    conn = ConnectMySQL().mysql()
    cur = conn.cursor()
    sql_msg_q_1 = "select tb_douban_movies.tb_movies_used_info.id, " \
                  "tb_douban_movies.tb_movies_used_info.actors " \
                  "from tb_douban_movies.tb_movies_used_info " \
                  "where tb_douban_movies.tb_movies_used_info.is_delete = false " \
                  "and tb_douban_movies.tb_movies_used_info.actors = '' ;"
    cur.execute(query=sql_msg_q_1)
    query_result = cur.fetchall()
    for row in query_result:
        row: tuple
        did = row[0]
        sql_msg_m_1 = "update tb_douban_movies.tb_movies_used_info " \
                      "set tb_douban_movies.tb_movies_used_info.actors = '无' " \
                      "where tb_douban_movies.tb_movies_used_info.id = {} ;".format(did)
        print(sql_msg_m_1)
        cur.execute(query=sql_msg_m_1)
        conn.commit()
    cur.close()
    conn.close()
