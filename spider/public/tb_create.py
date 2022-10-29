# coding: utf8
""" 
@File: tb_create.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/28 15:19
"""

from spider.public.mysqlserver_execute_command import ExecuteSQL


class CreateTables(ExecuteSQL):
    """创建数据"""
    
    def __init__(self):
        super(CreateTables, self).__init__()
        
    def c_tb_director_info(self):
        try:
            sql_msg = "create table if not exists tb_director_info (" \
                      "id int not null primary key auto_increment comment 'id'," \
                      "name varchar(50) not null unique comment '导演姓名'," \
                      "sex int not null comment '导演性别: 0-男, 1-女'," \
                      "introduction varchar(255) comment '导演介绍'," \
                      "link varchar(255) not null comment '导演详情链接'," \
                      "create_time datetime default current_timestamp comment '字段创建时间'," \
                      "modify_time datetime default current_timestamp on update current_timestamp comment '字段修改时间'," \
                      "is_delete boolean default false comment '是否逻辑删除'" \
                      ") charset utf8mb4;"
            super(CreateTables, self).exec_sql(sql_msg=sql_msg)
        except Exception as error:
            print(error)
            exit(1)

    def c_tb_player_info(self):
        try:
            sql_msg = "create table if not exists tb_player_info (" \
                      "id int not null primary key auto_increment comment 'id'," \
                      "name varchar(50) not null unique comment '演员姓名'," \
                      "sex int not null comment '演员性别: 0-男, 1-女'," \
                      "introduction varchar(255) not null comment '演员介绍'," \
                      "link varchar(255) not null comment '演员详情链接'," \
                      "create_time datetime default current_timestamp comment '字段创建时间'," \
                      "modify_time datetime default current_timestamp on update current_timestamp comment '字段修改时间'," \
                      "is_delete boolean default false comment '是否逻辑删除'" \
                      ") charset utf8mb4;"
            super(CreateTables, self).exec_sql(sql_msg=sql_msg)
        except Exception as error:
            print(error)
            exit(1)

    def c_tb_movies_info(self):
        try:
            sql_msg = "create table if not exists tb_movies_info (" \
                      "id int not null primary key auto_increment comment 'id'," \
                      "name varchar(50) not null unique comment '电影名称'," \
                      "director_id int not null comment '导演id'," \
                      "foreign key (director_id) references tb_director_info (id)," \
                      "assistant_director varchar(255) comment '副导演; 多个副导演使用,分隔'," \
                      "screenwriter varchar(255) not null comment '电影编剧; 多个编剧使用,分隔'," \
                      "player_master_id int not null comment '电影主演'," \
                      "foreign key (player_master_id) references tb_player_info (id)," \
                      "player varchar(100) not null comment '电影演员; 多个演员使用,分隔'," \
                      "first_play varchar(10) not null comment '电影首映时间'," \
                      "type varchar(30) not null comment '电影类型; 多个类型使用,分隔'," \
                      "country varchar(10) not null comment '制片国家; 多个国家使用,分隔'," \
                      "length int not null comment '电影时长'," \
                      "introduction varchar(255) default null comment '电影介绍'," \
                      "link varchar(255) not null comment '电影url'," \
                      "create_time datetime default current_timestamp comment '字段创建时间'," \
                      "modify_time datetime default current_timestamp on update current_timestamp comment '字段修改时间'," \
                      "is_delete boolean default false comment '是否逻辑删除'" \
                      ") charset utf8mb4;"
            super(CreateTables, self).exec_sql(sql_msg=sql_msg)
        except Exception as error:
            print(error)
            exit(1)

if __name__ == '__main__':
    # CreateTables().c_tb_director_info()
    # CreateTables().c_tb_player_info()
    # CreateTables().c_tb_movies_info()
    pass
